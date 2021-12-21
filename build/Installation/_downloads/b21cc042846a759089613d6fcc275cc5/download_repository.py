#!/usr/bin/env amspython
desc = """
This script is intended for downloading a copy of the AMS repository for offline usage.

It is intended for python 3.6+. AMSPython includes all necessary dependencies. 
If you wish to use a different python, external dependencies include requests,
and tqdm. Both can be installed from pypi using pip. 

The script can resume after interuption, and update files that have changed in size.

The latest instructions can be found online, in the installation manual:
https://www.scm.com/doc/Installation/Optional_Components.html#using-a-local-package-source
"""
import requests
from pathlib import Path
from requests.exceptions import HTTPError
from tqdm import tqdm
from urllib.parse import urlparse
import argparse


def sync_file_from_url(
    url: str, destination: Path, session: requests.Session, ignore_401=True
):
    """Synchronize a file from the given url to the specified destination using the provided session.

    Parameters
    ----------
    url : str
        Full length URL pointing to file on the webserver
    destination : Path
        Absolute path to the location to download the file to.
    session : requests.Session
        Session object with Authentication set, and other options.

    Notes
    -----
    If the file already exists, the size is checked. If the size matches, it won't be downloaded again.
    If the size does not match what is on the repository, the file will be deleted.
    Note that parent directories must already exist, this function will throw an error if not the case.

    Raises
    ------
    FileNotFoundError
        If directory is missing
    HTTPError
        If a communication error occurs for the download
    """
    # Retrieve URL header with size and access information
    head = session.head(url)
    filesize = int(head.headers.get("Content-Length", 0))

    if head.status_code == 401:
        if ignore_401:
            return
    head.raise_for_status()

    # If the file is not the right size, delete it
    if destination.exists():
        if destination.stat().st_size != filesize:
            destination.unlink()
        else:
            return

    # Stream data, track progress with tqdm
    with session.get(url, stream=True,) as r, destination.open("wb") as f, tqdm(
        unit="B",  # unit is bytes
        unit_scale=True,
        unit_divisor=1024,
        total=filesize,
        leave=False,
        desc=destination.name,
    ) as progress:

        written = 0
        for chunk in r.iter_content(chunk_size=10000):
            datasize = f.write(chunk)
            written += datasize
            progress.update(datasize)


def target_from_url(url: str, download_folder: Path) -> Path:
    """Takes the path from the URL and appends it to the folder specified to make a local download target."""
    prefix = "/Downloads/packages/"
    return download_folder / urlparse(url).path[len(prefix) :]


def files(listings_file: Path):
    """Provide the list of files. Note that newline characters are not stripped yet."""
    with listings_file.open("r") as openfile:
        return openfile.readlines()


def make_parser(desc):
    """Defines the parser"""
    parser = argparse.ArgumentParser(
        description=desc,
        epilog="All positional arguments are REQUIRED.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "LISTING_URL", help="Url pointing to the file listings for the repository."
    )
    parser.add_argument(
        "DOWNLOAD_FOLDER", help="A local directory for storing your download."
    )
    parser.add_argument("USER", help="Username for downloading from the website.")
    parser.add_argument("PASSWORD", help="Password for downloading from the website.")
    parser.add_argument(
        "--strict-authentication",
        action="store_true",
        help="If supplied this script will exit on 401 errors. By default, this script will skip files on 401 errors.",
        dest="strict_auth",
    )
    parser.add_argument(
        "--no-ssl",
        action="store_true",
        dest="no_ssl",
        help="Don't use SSL verification.",
    )
    return parser


if __name__ == "__main__":
    # Run the CLI
    parser = make_parser(desc)
    args = parser.parse_args()

    session = requests.Session()
    session.auth = (args.USER, args.PASSWORD)
    session.verify = not args.no_ssl

    # Resolve all unknowns in the path and make it absolute
    dl_path = Path(args.DOWNLOAD_FOLDER).expanduser().resolve().absolute()
    print("Downloading the listing...")

    listing_path = target_from_url(args.LISTING_URL, dl_path)
    listing_path.parent.mkdir(parents=True, exist_ok=True)
    sync_file_from_url(args.LISTING_URL, listing_path, session, ignore_401=False)

    print("Downloading files...[This could take a while].")
    for file_url in tqdm(
        files(listing_path),
        desc="Total file",
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
    ):
        url = file_url.strip()

        destination = target_from_url(url, dl_path)
        destination.parent.mkdir(parents=True, exist_ok=True)

        try:
            sync_file_from_url(
                url, destination, session, ignore_401=not args.strict_auth
            )
        except HTTPError as e:
            # One retry if connection was interrupted, otherwise crash
            if destination.exists():
                # clean partial file download that failed
                destination.unlink()

            sync_file_from_url(
                url, destination, session, ignore_401=not args.strict_auth
            )

    print("Done!")

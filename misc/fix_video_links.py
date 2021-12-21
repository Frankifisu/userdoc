from pathlib import Path
from html.parser import HTMLParser

# This script fixes the problem with the paths to the embedded videos, see SCMSUITE-5959.

video_locations = []

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if ('class', 'reference download internal') in attrs:
            for a in attrs:
                if a[0] == 'href':
                    url = a[1].split('/')
                    filename = url[-1]
                    folder   = url[-2]
                    if filename.lower().endswith('.mp4'):
                        video_locations.append((folder,filename))

parser = MyHTMLParser()

html_files = [str(p) for p in Path('build').glob('**/*.html') if 'Metadocumentation' not in str(p)]

# Find all video files we make available for download:
for path in html_files:
    with open(path, encoding='UTF-8') as f:
        html_content = f.read()
    # Quick pre-filter, so we don't need to parse all files ...
    if 'reference download internal' in html_content and '.mp4' in html_content:
        parser.feed(html_content)

# Fix all wrong links to these videos:
for path in html_files:
    with open(path, 'r', encoding='UTF-8') as f:
        orig_html_content = f.read()
    html_content = orig_html_content
    for folder,filename in video_locations:
        new_html_content = html_content.replace(f'/_downloads/{filename}', f'/_downloads/{folder}/{filename}')
        if new_html_content != html_content:
            print(f'-> Fixed path of video {filename} embedded in {path}')
            html_content = new_html_content
    if html_content != orig_html_content:
        with open(path, 'w', encoding='UTF-8') as f:
            f.write(new_html_content)

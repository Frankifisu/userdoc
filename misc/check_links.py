from pathlib import Path
from html.parser import HTMLParser
import os

# This simple program checks that the Sphinx inter-document links are pointing to an existing file.
# Inter-document links in Spinx are done using relative a relative path. 
# Example: a link from the Band manual to the Tutorials will look something like this in sphinx:
# `BAND GUI tutorials <../../Tutorials/BAND/BAND-GUI_tutorials.html>`__
# This will create the following html code:
# <a class="reference external" href="../../Tutorials/BAND/BAND-GUI_tutorials.html">BAND GUI tutorials</a>
# This script would check that the html file in "href" (../../Tutorials/BAND/BAND-GUI_tutorials.html) actually exists.

links = []

class MyHTMLParser(HTMLParser):
   def handle_starttag(self, tag, attrs):
      # Collects all relative links (starting with "..") and put them in the global variable links
      global links
      if ('class', 'reference external') in attrs:
         for a in attrs:
            if a[0] == 'href':
               link = a[1]
               if link.startswith('..'):
                  links.append(link)

def check_relative_links(links, current_file, html_files):
   for link in links:
      # Check that the number of "../" is correct:
      relative_path_ok = link.count('..'+os.sep) == (len(current_file.split(os.sep))-2)
      # Remove the anchor link:
      link_tmp = link.split('#')[0]
      # Remove all '../'
      link_tmp = link_tmp.replace('..'+os.sep,'')
      # Make the non-relative link:
      link_tmp = os.path.join('build', link_tmp)

      if not relative_path_ok:
         print("WARNING: improper relative path for {} (current_file = {}). Note: for intra-doc reference use Sphinx's :ref: and not a link.".format(link, current_file))
         continue 

      if not (link_tmp in html_files and relative_path_ok):
         print("WARNING: link '{}' in file '{}' not pointing to an existing file!".format(link,current_file))


parser = MyHTMLParser()

html_files = [str(p) for p in Path('build').glob('**/*.html')]

for path in html_files:
   html_content = open(path, encoding='UTF-8').read()
   if 'reference external' in html_content:
      links = []
      parser.feed(html_content)
      if len(links)>0:
         check_relative_links(links, path, html_files)

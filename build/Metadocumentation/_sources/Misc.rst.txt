Misc notes
##########

Block quotes
============

When building the html, Sphinx transforms certain reST constructs into html block quotes. Since we do not want block quotes in our html files (because of some search engine optimization issue), the **build_doc.sh** script warns you if it finds any in the html files. This is a (probably incomplete) list of constructs that might lead to block quotes in the html:

* Indentation with 3 spaces (you should use 2-spaces indentation). This is of course very weird...
* indented lists

Trunk and Fixes
===============

There is a small (but important) difference between the sphinx-themes for the trunk and fixes versions:

The line ``"<META name="ROBOTS" content="NOINDEX, NOFOLLOW">"`` in ``userdoc/trunk/themes/scm_theme/layout.html`` is there for preventing google from indexing the trunk version, which is now publicly available at scm.com/doc.trunk


Footer, css and related
=======================

Marc Mouthaan made ``footer.html``, ``layout.html`` and ``static/css/*.css`` in ``themes/scm_theme`` to make the same look/feel as WP site. Fedor added the cookie consent javascript part to ``layout.html`` to comply with GDPR cookie-loading only after consent in June 2018. This was added retro-actively also to fix2016. This should change to an include so as not to have the cookiebanner for offline documentation.




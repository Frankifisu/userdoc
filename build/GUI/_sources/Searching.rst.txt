Searching
*********

In AMSinput there is a search icon in the top-right corner.
Click on it to bring up a search box.
Searching will be performed automatically when you enter text in the search box.


You will search multiple things at the same time:

- matching panels with input options in AMSinput (from the panel bar)
- documentation
- molecules

The search will be restricted to panels and documentation that belong to the 
currently selected program (ADF, BAND, DFTB, ...). In these panels, it will find
any panel that contains your search string, including the matching program key.


Prefix: key

If you start your search with "key " (without quotes), you will restrict your search to 
fields related to matching input keys only. 
This will allow you to locate an input option very quickly.

Prefix: all

If you start your search with "all " (without quotes), the search will be global
for both the panel search and documentation search.
Thus it will not be restricted to the currently selected program.


The molecule search will search a (local) database with some common molecular structures.
Currently it consists of a roughly 1800 molecules optimized with ADF for use with COSMO-RS,
and of the molecules found in the NCI database (NCI-Open_09_03.sdf, 
see http://cactus.nci.nih.gov). The molecules in the NCI database have been filtered 
to include only molecules with names and xyz coordinates, and most CAS numbers have
been removed for legal reasons.
Also periodic structures are available: zeolites (from the `Database of Zeolite Structures <http://www.iza-structure.org/Databases>`__),
many simple crystal structures, and a set of complex crystals included with the MOPAC distribution.

As the structures come from an external source we can not guarantee that the found structures
will be correct. So please check them!

In total roughly 35000 molecules are available. 


To clear the search results at any time, also when the search box is no longer visible, 
use the Escape key.


Only the locally included documentation and molecule structures will be searched.
No internet search will be performed.

Panel search details
====================

All text belonging to the panels will be searched: panel titles, labels for input options,
headers, text in pull-down menus, and text in help balloons.

You can use the * and ? wildcards: the * matches anything, the ? matches any single character.
The search string will be broken into words, and only results containing all words will be found.
Use double quotes (") around text to search for exactly that phrase.
The words to search for are implicitly surrounded by * wildcards, so text matching will happen 
even in the middle of a word.

The names of the found panels will be listed. When you click on one of them, it will be activated.
Options not matching the search string will be dimmed. If an option is not dimmed, it matches
either directly, by it's help text, or by the page title.

Use the arrows next to the search loupe to quickly loop through the found panels.


Key search details
==================

To search for input fields that have to do with a particular input key, you can use the 
key search. To do this, start your search string with "key " (without the quotes).
This will restrict the panel search to find only items that set or change the matching key.

You can use the * and ? wildcards: the * matches anything, the ? matches any single character.
The search string will be broken into words, and only results containing all words will be found.
Use double quotes (") around text to search for exactly that phrase.
The words to search for are implicitly surrounded by * wildcards, so matching will happen 
even in the middle of a word.

For example, searching for 

key integration

will show you what input options in the GUI will set the INTEGRATION key.

The names of the found panels will be listed. When you click on one of them, it will be activated.
Options not matching the search string will be dimmed. If an option is not dimmed, it matches
either directly, by it's help text, or by the page title.

Use the arrows next to the search loupe to quickly loop through the found panels.


Documentation search details
============================

The included documentation (in html format) will be searched using the Swish-e search engine.
You will be searching for words. If you specify more you will get matches that contain both
words, in any order.

The (shortened) titles of the found documentation pages will be listed. If you point at an item
with your mouse, it will show the full title. Click on it to open that item with your default
browser. Note that you will be viewing local documentation, not the SCM web site.

When staring, only the first 5 documentation matches will be shown. To view all results, click
on the arrow on the right side of the 'Documentation' header in the search results.
Click on the same arrow again to show only the first 5 results again.

You can use the * wildcard to match anything, but only at the end of an word.
You can use the ? wildcard to match a single character, but NOT at the beginning of an word.
You can also perform complex searches using logical operators (and, or, not) and parenthesis.
If no operator is specified between words, the and operator is used (both words need to be found)
Finally, you can search for an exact phrase using quotes.

For example: integration and not accuracy
             integration or accuracy
             integration key
             "integration key"

The search will be restricted to the parts of the documentation relevant to the module you are 
using. Thus, when searching from AMSinput with ADF active, the BAND documentation 
will not be searched.

If you prefix your search with "all " (without the quotes), all documentation will be searched.

For more information on Swish-e: http://swish-e.org/


Molecule search details
=======================

The included database of molecules will be searched. You can search for the IUPAC name,
the molecule formula, the CAS number, and sometimes alternative names.
Note that the CAS number search will often fail as only a few CAS numbers are included.

You can use the * and ? wildcards: the * matches anything, the ? matches any single character.
The search string will be broken into words, and only results containing all words will be found.
Use double quotes (") around text to search for exactly that phrase.
The words to search for are implicitly surrounded by * wildcards, so text matching will happen
even in the middle of a word.

When you start your search string with "=" (an equal sign, no quotes), 
no wild cards will be added automatically.

When you move the mouse over one of the found molecules, you will get full details including the
origin of the entry (optimized by ADF, or from the NCI database).

When you click on the desired search result, that particular molecule will be imported.


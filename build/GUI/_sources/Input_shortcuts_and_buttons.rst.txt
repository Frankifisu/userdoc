Input: buttons
**************

Searching
=========

At the top right in the panel bar you will find a Search tool. You can activate it by clicking on it, or by using  the ctrl/cmd-F shortcut. 

After activating it, a small field will pop-up that allows you to enter your search text. 

When you enter some text in the search field, the search will start immediately and the results will be presented below the search text. The results are divided in several sections: 

Panels: a list of all panels that match the search text. All texts on a panel will be searched: titles, menus, help text and associated keys. When you click on one of the panel search results that panel will be activated, and the items matching your search query will be marked. This is a very convenient way to find a particular input option. The search is restricted to panels belonging to the currently active method (thus, while in ADF input mode you will not find BAND input panels). 

Documentation: a list of matching documentation pages. If you click on it, that page will be shown in your browser. Note that this uses the local documentation, it does not contact the SCM web site. Again, the search is restricted to documentation that belongs to the currently active method. 

Molecules: a list of matching molecules. The match may for example be in the name or in the molecule formula. If you click on a match, that molecule will be imported. The list of molecules is a mix of some ADF optimized molecules, and of results taken from the NCI-Open database (see http://cactus.nci.nih.gov). Again, all information is contained in the ADF distribution, the search will not contact external sources. In total about 35000 molecules are included. 

Crystals: a list of matching crystals. The match may be in the name or formula. Most of the crystals are simple common crystals are found in many  textbooks. On the MOPAC web site there is a list of crystals that have been optimized using MOPAC. Those are also included. Finally, the zeolite frameworks from the  `IZA-SC database <http://www.iza-structure.org/databases/>`__ are available. 

When starting, at most five matches will be shown in each section. At the right side of the section headers (Panels, Documentation, Molecules) you will spot a triangle pointing to the right. If you click on it, you will open that particular section and many more results will be shows, if available. 

Pressing the "?" (to the right of the search text field) will bring up a detailed description of the search facility. It will explain how to do more complex searches. 

If you move your mouse above one of the search results, without clicking on it, a balloon will pop up showing more details about that particular match. For the documentation matches it will tell you from what manual the result is, and from which chapter. For molecules it will give some more information about that molecule, like names, sometimes a CAS number, and what the source of the data is (for example, optimized using ADF, or from the NCI-Open database). 

After typing a search text, you can also use the up and down arrow keys to select a particular search result, and then press the Return key to open that result. When starting with ctrl/cmd-F this means you can perform the search and accept result without using the mouse. 

The ">" details buttons
=======================

In many panels in AMSinput you will find buttons with an arrow (or a greater-than sign). These buttons will activate a panel showing more details for some particular feature. 

For example, the ">" button to the right of the Task option in AMSinput will activate a panel that allows you to set details for the current task. Thus details for a geometry optimization, or details for a transition state search. 

It depends on the context and sometimes on the active options to which panel the buttons link. In all situations it should be intuitive, just try it out. 

Using the "?" info buttons
==========================

Some panels in AMSinput have an "?" button (just as the search pop-up). When you press the "?" button, a new page will open with much more background information on some feature. 

For example, the "?" button in the search pop-up will show a description of the search syntax.  And the "?" button next to the basis set (in the Basis detail panel) will show more information about the basis sets. 

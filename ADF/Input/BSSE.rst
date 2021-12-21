.. index:: BSSE 
.. index:: basis set superposition error 

Basis Set Superposition Error (BSSE)
************************************

The :ref:`Ghost Atom <GHOST>` feature enables the calculation of Basis Set Superposition Errors (BSSE). The idea is as follows. In a normal calculation of the bonding energy of a molecule c, composed of fragments a and b, one compares the total energies of c vs. those of isolated a and isolated b added together. In ADF this can be done in one stroke by running c from fragments a and b. 

The BSSE is determined as the bonding energies of a pseudo-molecule d composed of (1) a plus a ghost b and (2) b plus a ghost a. The ghost atoms in the calculations are at their normal positions in the true molecule c, and they have their normal basis (and fit) functions. However, they do not have a nuclear charge and no electrons to contribute to the molecule. To set such a calculation up one needs first to make the appropriate ghost basis set files: for each involved atom, copy the basis set file that was used for its creation and modify it so as to remove the frozen core. Next, Create the ghosts with zero mass and zero nuclear charge. Apply these ghost fragments in the BSSE runs. 


.. seealso::
    
  * :ref:`example BSSE_CrCO6`
  * Tutorial: `Basis set superposition error (BSSE) <../../Tutorials/StructureAndReactivity/BSSEDoubleHybrids.html>`__


from functools import reduce

# Make sure this script was called correctly
if not 'resultsdir' in globals():
    print("\n USAGE: $AMSBIN/plams new-cross-link-density.py -v resultsdir=[path to .results folder]\n")
    quit()

# Load the job associated with that .results folder
bondboost = AMSJob.load_external(resultsdir)

# determine number of possible CN bonds from first frame
max_CN_Bonds = 0
pre_existing_CN_Bonds = 0
iSys = bondboost.results.get_history_molecule(1)
iSys.guess_bonds()
for bond in iSys.bonds:
        if bond.atom1.symbol == "N" and bond.atom2.symbol == "H":
            max_CN_Bonds += 1
        elif bond.atom1.symbol == "H" and bond.atom2.symbol == "N":
            max_CN_Bonds += 1
        elif bond.atom1.symbol == "C" and bond.atom2.symbol == "N":
            pre_existing_CN_Bonds += 1
        elif bond.atom1.symbol == "N" and bond.atom2.symbol == "C":
            pre_existing_CN_Bonds += 1

nEntries = bondboost.results.readrkf('History', 'nEntries')
for iHistEntry in range(2,nEntries+1):
    # Get the geometry for the accepted MC step
    iSys = bondboost.results.get_history_molecule(iHistEntry)
    iSys.guess_bonds()
    # Find N atoms
    CN_Bonds = 0
    for bond in iSys.bonds:
        if bond.atom1.symbol == "C" and bond.atom2.symbol == "N":
            CN_Bonds += 1
        elif bond.atom1.symbol == "N" and bond.atom2.symbol == "C":
            CN_Bonds += 1
    cross_link_density = (CN_Bonds-pre_existing_CN_Bonds)/max_CN_Bonds
    print("({:4d}/{:4d}) {:2.3f} {:2.3f}".format(iHistEntry,nEntries, CN_Bonds, cross_link_density))

# compute density from lattice vectors and total mass, only for last frame
latticevecs = bondboost.results.readrkf('Molecule', 'eeLatticeVectors') 
latticevecs = list(filter(lambda a: a != 0, latticevecs))
volume = reduce((lambda x, y: x * y), latticevecs) * 0.14818 #convert Bohr**3 to Ang**3
masses = bondboost.results.readrkf('Molecule', 'AtomMasses')
mass = sum(masses)
print("\n  Final density: {:2.3f} \n  Cross-linking ratio: {:2.3f} \n".format(mass/volume*1.6601, cross_link_density))


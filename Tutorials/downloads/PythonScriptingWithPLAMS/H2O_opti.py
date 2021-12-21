# H2O_opti.py
# Geometry optimization of a water molecule using ADF

# Create the molecule:
mol = Molecule()
mol.add_atom(Atom(symbol='O', coords=(0,0,0)))
mol.add_atom(Atom(symbol='H', coords=(1,0,0)))
mol.add_atom(Atom(symbol='H', coords=(0,1,0)))

# Initialize the settings for the ADF calculation:
sett = Settings()
sett.input.ams.task = 'GeometryOptimization'
sett.input.adf.basis.type = 'DZP'
sett.input.adf.xc.gga = 'PBE'

# Create and run the job:
job = AMSJob(molecule=mol, settings=sett, name='water_GO')
job.run()

# Fetch and print some results:
energy = job.results.get_energy()
opt_mol = job.results.get_main_molecule()
bond_angle = opt_mol.atoms[0].angle(opt_mol.atoms[1], opt_mol.atoms[2])

print('== Water optimization Results ==')
print('Bonding energy: {:8.2f} kcal/mol'.format(Units.convert(energy, 'au', 'kcal/mol')))
print('Bond angle:     {:8.2f} degree'.format(Units.convert(bond_angle, 'rad', 'degree')))
print('Optimized coordinates:')
print(opt_mol)

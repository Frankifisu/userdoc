#!/usr/bin/env amspython
#########################
# PLAMS example for the TiO2 surface relaxation tutorial using VASP via the AMS driver
#    A TiO2(001) slab is constructed using functionality from ASE
#    VASP settings are set 
#    Settings for the constrained geometry optimization are set
#    The job is run
########################

from scm.plams import *
import ase
import os

####### general VASP settings #################
vasp_command = 'MUST_BE_FILLED_IN' # command to execute vasp, for example 'mpirun -np 4 vasp'
# Paths to POTCAR files for each element. 
# Note: If the files are compressed and called POTCAR.Z, you must first uncompress them.
potcar_dict = { 'Ti': '/some/path/PAW_PBE/Ti/POTCAR',  
                'O' : '/some/path/PAW_PBE/O/POTCAR'}
only_preprocessing = 'No' # set to 'Yes' to not run VASP, but instead only generate the VASP input for the first geometry optimization step
############################################## 

init() #PLAMS initialization

# With external engines, it is necessary to set the environment variable NSCM to 1
os.environ['NSCM'] = '1'

def get_rutile001_slab(nlayers=4, vacuum=10.0):
    """Returns a PLAMS molecule of a TiO2 rutile (001) slab, with the given number of layers and vacuum gap (in angstrom). 
    The atoms are returned in ascending order according to the z coordinate."""
    from ase.build import cut, add_vacuum
    from ase.spacegroup import crystal
    import numpy as np
    # experimental rutile TiO2 lattice parameters
    a = 4.59
    c = 2.96

    rutile = ase.spacegroup.crystal(['Ti', 'O'], 
                                    basis=[(0., 0., 0.), (0.3, 0.3, 0.0)], 
                                    spacegroup=136, 
                                    cellpar=[a, a, c, 90, 90, 90])


    # the [1,0,0] and [0,1,0] directions are parallel to the surface
    rutile_001 = ase.build.cut(rutile, a=[1,0,0], b=[0,1,0], nlayers=nlayers)

    # add vacuum gap
    ase.build.add_vacuum(rutile_001, vacuum)

    # shift the slab to the center of the vacuum gap along z (optional)
    old_positions = rutile_001.get_positions()
    mean_z_coord = np.mean(old_positions[:, 2])
    new_positions = old_positions.copy()
    new_positions[:, 2] += rutile_001.cell[2,2]/2.0 - mean_z_coord
    rutile_001.set_positions(new_positions)

    # sort the atoms with respect to z for easy extraction of the central atoms later
    rutile_001 = ase.build.sort(rutile_001, tags=new_positions[:, 2])

    # convert the ASE Atoms object to a PLAMS Molecule
    plams_mol = fromASE(rutile_001)
    return plams_mol

def list_of_elemental_properties(mol, properties_dict):
    """ If the order of the atoms the molecule are for example [Ti, O, O, Ti, O, O]
        then the VASP POSCAR will contain the lines
            Ti O Ti O
            1  2 1  2
        This function takes in a property of some element (e.g. the Hubbard U value, or path the the POTCAR file)
        and returns a list of the properties where identical elements in a row have been collapsed into
        a single value.

        mol: a PLAMS molecule
        properties_dict: a dictionary

        Example: mol.symbols == ['Ti', 'O', 'O', 'Ti', 'O', 'O'] properties_dict == {'Ti': 'prop_Ti', 'O': 'prop_O'}
                 return: ['prop_Ti', 'prop_O', 'prop_Ti', 'prop_O']
    """
    ret_list = []
    prev_symbol = None
    for at in mol:
        if at.symbol not in properties_dict:
            raise RuntimeError("Could not find element {} in {}".format(at.symbol, properties_dict))
        if prev_symbol is None or at.symbol != prev_symbol: 
            ret_list.append(properties_dict[at.symbol])
        prev_symbol = at.symbol
    return ret_list

def create_potcar(out_path, molecule, potcar_dict):
    """ concatenate the POTCAR files from potcar_dict according to the atoms in molecule. Writes the resulting POTCAR to out_path (absolute path) """
    potcar_files = list_of_elemental_properties(molecule, potcar_dict)
    with open(out_path, 'w') as potcar_out:
        for potcar_file in potcar_files:
            with open(potcar_file, 'r') as potcar_in:
                for line in potcar_in:
                    potcar_out.write(line)


# Construct the system using the get_rutile011_slab function
mol = get_rutile001_slab(nlayers=4, vacuum=8.08)
# Alternatively, the system can be set up in the GUI and exported in the .xyz format. It can then be read in using:
# mol = Molecule('filename.xyz')

vasp_s = Settings()
vasp_s.VASPExec = vasp_command
vasp_s.Smearing = '0.1 [eV]'
vasp_s.XC = 'PBE'
vasp_s.nk1 = 3
vasp_s.nk2 = 3
vasp_s.nk3 = 1
vasp_s.LDAU = 'Yes'
vasp_s.LMAXMIX = 4
vasp_s.LDAUU = ' '.join(list_of_elemental_properties(mol, {'Ti': '3.0', 'O': '0.0'}))
vasp_s.LDAUJ = ' '.join(list_of_elemental_properties(mol, {'Ti': '0.0', 'O': '0.0'}))
vasp_s.LDAUL = ' '.join(list_of_elemental_properties(mol, {'Ti': 'd', 'O': 'Disable'}))
# use PLAMS free-form text _1, _2, etc., for additional INCAR settings
vasp_s.Misc._1 = "ALGO = Fast"
vasp_s.OnlyPreprocessing = only_preprocessing

s = Settings()
#########
# Settings for the external engine
########
# the Execute and InputDefinition are required
s.input.External.Execute = os.path.join(os.environ['AMSBIN'], 'amspython') + ' ' + \
                           os.path.join(os.environ['AMSHOME'], 'scripting', 'standalone', 'external_engines', 'vasp.py')
s.input.External.InputDefinition = os.path.join(os.environ['AMSBIN'], 'input_def', 'vasp.json')
s.input.External.Input = vasp_s

#########
# AMS driver settings (geometry optimization)
#########
s.input.ams.Task = 'GeometryOptimization'
# there are 12 atoms, so the one-based indices for the six central atoms are 4, 5, 6, 7, 8, 9
# since the atoms were sorted with respect to z-coordinate
s.input.ams.Constraints.Atom = list(range(4, 10))

##########
# Define the AMS job
#########
job = AMSJob(name='VASP_PBE_U_TiO2_slab', settings=s, molecule=mol)

# the POTCAR file needs to be created in the run directory before VASP is run
# this can be done by defining a "prerun" method for the job
@add_to_instance(job)
def prerun(self):
    create_potcar(os.path.join(self.path, 'POTCAR'), self.molecule, potcar_dict)

########
# Run the job
#######
job.run()

finish() #PLAMS finish


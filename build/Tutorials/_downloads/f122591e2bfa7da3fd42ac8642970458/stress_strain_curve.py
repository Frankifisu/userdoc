import sys
import os
from scm.plams import *
import numpy as np 

#===========================
#        Calculate 
#===========================
#
# print help and exit
#
def help_n_exit(message):
    print(message)
    sys.exit(1)

convrs_MPa = 1/3.398929167906144e-8 


#----------------------------------------------------------------------#
#                          MAIN                                        #
#----------------------------------------------------------------------#
if __name__ == '__main__':
    #
    # stop if this script is called without
    # the kf-file as argument
    #
    if len(sys.argv) != 2:
        help_n_exit("\n USAGE: " + str(sys.argv[0]) + " [name of job]\n")     
    kf_filename = f"{sys.argv[1]}.results/ams.rkf"
    #
    # Initialize the PLAMS KFReader 
    #
    try:
        kfreader = KFFile(kf_filename)
    except:
        exception = sys.exc_info()[0]
        help_n_exit("\n tried to initialize KFFile: " + kf_filename + " ->  Error: %s " % exception + "\n")

    # Iterators for the History/MDHistory sections
    mdhistory = KFHistory(kfreader, "MDHistory")
    history = KFHistory(kfreader, "History")



    # Outputfile
    #   
    fout = open('stress-strain-curve.csv', 'w')         
    fout.write("# strain_x, strain_y, strain_z, stress_xx, stress_yy, stress_zz\n")
    #
    # Initial lattice vectors
    #
    a, _, _, _, b, _, _, _, c = kfreader.read('History','LatticeVectors(1)')

    for step, lattice, ptens_Voigt in zip(mdhistory.iter("Step"), history.iter("LatticeVectors"), mdhistory.iter("PressureTensor")):    
        if step <=0:             
            continue

        # Read new lattice vectors and calculate strain
        a_new, _, _, _, b_new, _, _, _, c_new = lattice
        
        # Calculate the engineering normal strain 
        Strain_a = (a_new - a)/a 
        Strain_b = (b_new - b)/b
        Strain_c = (c_new - c)/c 
        
        # Read the stresses, convert from pressure, and to MPa
        Stress_XX, Stress_YY, Stress_ZZ, _, _, _ = -1.0 * np.array(ptens_Voigt) * convrs_MPa

        # Write to file
        fout.write("{:2.4f} {:2.4f} {:2.4f} {:2.12f} {:2.12f} {:2.12f}\n".format(Strain_a,Strain_b,Strain_c, Stress_XX,Stress_YY,Stress_ZZ))

fout.close()      
print("\n results written to file stress-strain-curve.csv \n")
from functools import reduce
import sys
import os

#Make sure this script was called correctly
if not 'resultsdir' in globals():
   print("\n USAGE: $AMSBIN/plams densities.py -v resultsdir=[path to .results folder]\n")
   quit()

# Average how many frames
average_frames = 10

#Load the job associated with that .results folder
mdresults = AMSJob.load_external(resultsdir)

# use the PLAMS KF reader to read from the ams.rkf binary output file
kf = KFReader(mdresults.results['ams.rkf'])
mdhist = KFHistory(kf, "MDHistory")
hist = KFHistory(kf, "History")
counter = 1
temperature = 0.0
mass = 0.0
densities = 0.0
a_vec = 0.0
b_vec = 0.0
c_vec = 0.0
# iterate through the frames of the trajectory
for T in mdhist.iter("Temperature"):
    latticevecs = kf.read('History', 'LatticeVectors({:d})'.format(counter))
    latticevecs = list(filter(lambda a: a != 0, latticevecs))
    volume = reduce((lambda x, y: x * y), latticevecs) * 0.14818 #convert Bohr**3 to Ang**3
    masses = mdresults.results.readrkf('Molecule', 'AtomMasses')
    temperature += T
    mass += sum(masses)
    a_vec += latticevecs[0]
    b_vec += latticevecs[1]
    c_vec += latticevecs[2]
    # calculate densities [g/mL] from masses and volume
    densities += sum(masses)/volume*1.6601
    if (counter-1) % int(average_frames) == 0 and counter > 1:
        print("{:4.1f} {:2.3f} {:2.3f} {:2.3f} {:2.3f}".format(temperature/average_frames,densities/average_frames, a_vec/average_frames, b_vec/average_frames, c_vec/average_frames))
        mass = 0.0
        temperature = 0.0
        densities = 0.0
        a_vec = 0.0
        b_vec = 0.0
        c_vec = 0.0
    counter += 1
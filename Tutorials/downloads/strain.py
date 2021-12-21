from functools import reduce
import sys
import os

#Make sure this script was called correctly
if not 'resultsdir' in globals() or not 'startstep' in globals():
   print("\n USAGE: $AMSBIN/plams strain.py -v resultsdir=[path to .results folder] -v startstep=[STARTSTEP]\n")
   quit()

#Load the job associated with that .results folder
mdresults = AMSJob.load_external(resultsdir)

# use the PLAMS KF reader to read from the ams.rkf binary output file
kf = KFReader(mdresults.results['ams.rkf'])
mdhist = KFHistory(kf, "MDHistory")
hist = KFHistory(kf, "History")
counter = 1
print('# T[K] a[Å]     b[Å]    c[Å]    V [Å**3]')
# iterate through the frames of the trajectory
for T in mdhist.iter("Temperature"):
    step = kf.read('History', 'Step({:d})'.format(counter))
    latticevecs = kf.read('History', 'LatticeVectors({:d})'.format(counter))
    latticevecs = list(filter(lambda a: a != 0, latticevecs))
    volume = reduce((lambda x, y: x * y), latticevecs)
    if step >= int(startstep) and step <= 650000:
        print("{:4.1f} {:2.3f} {:2.3f} {:2.3f} {:5.3f}".format(T,latticevecs[0], latticevecs[1], latticevecs[2], volume))
        temperature = 0.0
    counter += 1

.. index:: execution of COSMO-RS

Running the COSMO-RS program
****************************

Running the COSMO-RS program involves the following steps: 

+ Construct an ASCII input file, say in.

+ Run the program by typing (under UNIX): $AMSBIN/crs < in > out 


+ Move / copy relevant result files (in particular CRSKF) to the directory where you want to save them, and give them appropriate names.

+ Inspect the standard output file out to verify that all has gone well.

Note that in the one can also put the call to $AMSBIN/crs inside a script, which could be named, for example, 'example.run'.
Such shell script 'example.run' needs be executable, if it isn't you will need to make it executable, e.g. ``chmod u+x example.run``.
The 'example.run' file needs to be executed as a shell script, not as input to $AMSBIN/crs.


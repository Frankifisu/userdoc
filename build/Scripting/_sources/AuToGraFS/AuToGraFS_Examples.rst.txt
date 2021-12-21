AuToGraFS Examples
############################

the following examples work with all calculators of the Amsterdam Modeling Suite. Any python script using these libraries should be launched using the "$AMSBIN/amspython" binary.


Generation of all available pillared SURMOF
-------------------------------------------

::

    # Required imports
	from scm.autografs import *
    from itertools import combinations_with_replacement

	# create the  generator object
	mofgen = autografs.Autografs(path="./my_database/")

	# the SURMOF family of frameworks is
	topology = "pcu"
	
	# get all available linkers, center, pillars for the pcu topology
	centers = mofgen.get_available_centers(topology=topology)
	for center in centers:
		# the pcu topology accepts up to three different linkers.
		# here, we'll use two and a pillar
	    linkers = mofgen.get_available_linkers(topology=topology, center=center)
	    for linker in combination_with_replacement(linkers, 2):
	    	pillars = mofgen.get_available_pillars(topology=topology, center=center)
	    	for pillar in pillars:
	    		label = "{0}-{1}-{2}".format(center, linker,pillar)
	    	    # generate this particular framework
	    	    framework = mofgen.make(label=label,
	    	    						topology=topology,
	    	    						center=center,
	    	    						linker=linker,
	    	    						pillar=pillar)
	    	    # write the UFF inpufile under "label.run" and "label.ams"
	    	    framework.write()



Generation of a defectuous UIO-66 MOF from custom files
-------------------------------------------------------

::

    # Required imports
	from scm.autografs import *
	from random import gauss

	# get the building units as Fragment objects
	center = utils.read_inp("UIO66_center.inp")
	linker = utils.read_inp("UIO66_linker.inp")

	# instantiate the generator
	mofgen = autografs.Autografs()

	# generate the MOF
	mof = mofgen.make(label="UIO66", topology="bcu", center=center, linker=linker)

	# get the 3*3*3 supercell
	supercell = mof * (3,3,3)

	# introduce 10 defects in a gaussian distribution around the center of the supercell 
	# the connections are capped with hydrogen.
	indices = []
	mu    = len(supercell)/2
	sigma = len(supercell)/4
	number_of_defects = 10
	while len(indices) < number_of defects:
	    index = int(abs(gauss(mu, sigma)))
	    if (index not in indices) and index < len(supercell):
	        indices.append(index)
	supercell.insert_defect(indices = indices))

	# view resulting framework in adfinput
	supercell.view()


Generation of conformers in the IRMOF-5
---------------------------------------

::
	
	# Required imports
	from scm.autografs import *
	from itertools import combinations_with_replacement

	# instantiate the generator
	mofgen = autografs.Autografs()

	# generate the MOF
	mof = mofgen.make(label="IRMOF-5", topology="pcu", center="mof5", linker="benzene")

	# get the indices of the benzenes in the mof
	benzenes = mof.get_linkers()
	choice_angles = [0.0,45.0,90.0]

	# generate all possible combinations
	iteration = 0
	for angles in combinations_with_replacement(choice_angles, 3):
	    conformer = mof.copy()
	    for benzene, angle in zip(benzenes, angles):
	        conformer.rotate_fragment(index=benzene, angle=angle)
	    conformer.write(name="conformer-{0}".format(iteration))
	    iteration += 1


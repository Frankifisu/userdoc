The Molecule Gun
****************

The molecule gun allows you to "shoot" (add with velocity) a molecule into the simulation box. 
Molecules can be continuously added to the simulation or only once. The initial position 
as well as the initial velocity can be pre-set or random w.r.t. to all or a selection of X,Y,Z-components.
Possible applications of the molecule gun include e.g. the simulation of enforced collisions or deposition 
processes on surfaces. 

.. seealso:: 

  `Mol. Gun GUI tutorial <../Tutorials/MolecularDynamicsAndMonteCarlo/MoleculeGun.html>`__

The molecule gun requires an additional input file called **addmol.bgf**. 
It contains the geometry of the particle to be shot in BGF format and some additional keywords.

The following keywords may be specified in the **addmol.bgf** file:

**Input Keywords**

+ *FREQADD*    –   Add new molecule every N-th step but not before the iteration specified in FIRSTADD
+ *FIRSTADD*   –   Add the first molecule at iteration N
+ *VELADD*     –   Velocity of the added molecule: 1 - random, 2 - specified in the addmol.vel file, 3 - via a temperature specified with *TADDMOL* 
+ *STARTX*     –   The initial X coordinate of the added molecule, random if not specified
+ *STARTY*     –   The initial Y coordinate of the added molecule, random if not specified
+ *STARTZ*     –   The initial Z coordinate of the added molecule, random if not specified
+ *ADDIST*     –   Minimum distance from the molecule to other atoms for successful addition
+ *NATTEMPT*   –   The program will try to add a molecule N times until the ADDIST criterion is met
+ *TADDMOL*    –   for VELADD=1|3: temperature for the velocity of the molecule as a whole 
+ *ROTATE*     –   The molecule is rotated randomly before being added
+ *SIGMAX*     –   sigma parameter for the Gauss distribution of the initial X coordinate around STARTX
+ *SIGMAY*     –   sigma parameter for the Gauss distribution of the initial Y coordinate around STARTY
+ *SIGMAZ*     –   sigma parameter for the Gauss distribution of the initial Z coordinate around STARTZ
+ *VELXYZ*  (Vx Vy Vz)  –   for VELADD=3: the direction vector for the initial velocity of the added molecule
+ *SIGMAT*     –   for VELADD=1|3: standard deviation for TADDMOL
+ *TDISPER*    –   for VELADD=3: each atom's velocity is modified with V{x,y,z}=sqrt(RT/m)*random_normal(0,1)


**Example** 

The following example **addmol.bgf** file will create one carbon atom every 1000th iteration starting from iteration 500. The added atom will have an initial temperature of 800K and will initially move in the positive direction along the Z axis.

::

    BIOGRF 200
    DESCRP C
    REMARK Created by AMSinput
    VELADD 3
    FIRSTADD 500
    FREQADD 1000
    STARTX 1.671997104
    STARTY -4.00486678
    STARTZ -0.3259654382
    ROTATE 1
    TADDMOL 800
    VELXYZ 0.0 0.0 5.0
    HETATM     1 C                   1.67200  -4.00487  -0.32597 C      1 1  0.0 
    END

.. tip::
  
  Use the GUI to setup a molecule gun calculation and edit the .run file created by the GUI to  
  minimize typos. The section *addmol.bgf* is found at the end of the run file just before the *control* section. 

**Changes with respect to the original reac program**

It is possible to add some randomness both to the pre-set position and to the velocity: the SIGMA{X,Y,Z} keywords specify a standard 
deviation value for the Gauss distribution around the START{X,Y,Z} values, respectively. If "ROTATE 1" is specified, the molecule will 
be rotated randomly around its geometric center before being added to the system.


A VELADD=3 option has been added. With this option, it is possible to specify the velocity vector's direction via VELXYZ. 
This vector is normalized so the exact magnitude of its components does not matter. The magnitude of the velocity along this vector is 
determined by the TADDMOL and SIGMAT parameters as sqrt(3nRT/M), where T=TADDMOL + SIGMAT*random_normal(0,1), n - number of atoms in the molecule, 
R - gas constant, M - molar mass. Additionally, the velocity of each atom may be modified with a random component based on the temperature specified 
by the TDISPER keyword. On average, the total temperature of the added molecules should be close to TADDMOL+TDISPER.


Molecules will never be added before the step specified by the FIRSTADD keyword. Thus, a molecule will always be added at the FIRSTADD step and then at 
every iteration divisible by FREQADD. If, for example, FIRSTADD=1999 and FREQADD=1000 then the first molecule will be added at iteration 1999, 
the second at iteration 2000 and then every 1000-th iteration after that.

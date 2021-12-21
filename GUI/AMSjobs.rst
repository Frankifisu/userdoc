.. _metatag ADFJOBS: 

AMSjobs
#######

Jobs
****

Job list: per folder or global
==============================

When AMSjobs starts, it will generate a list of jobs for you by scanning the local directory. All files that have the same file name, with  only a different extension, will be considered to be one job. A job may also contain a directory, it should have the .results as extension. 

AMSjobs can also show a global list of jobs. All recent jobs that it knows about (by previously scanning a directory, or by running them) are shown. This typically can be a huge list, and it is limited (currently) to 500 most recent jobs. The big advantage is that you do not need to remember where you saved a job, it will automatically show in the global list. To switch between the two modes (showing only jobs in the current directory, or showing all known jobs) use the toggle switch at the right bottom corner. 

If you are viewing the global list of jobs, you can use the **View → Job Location** menu command to show where on your disk the jobs  are located. For each job one extra line will be displayed with this information. 

The job list refreshes automatically when needed. You can force a refresh via the **Job → Refresh List** menu command, or by pressing F5. For each job you will see: 

The Filter command determines what kind of jobs will be shown. For example, you can choose not to show directories, or only ADF jobs. 

At the bottom right you will find a toggle button. This button will toggle between the two modes of AMSjobs: show all jobs, or show the jobs per folder. 

Job status (including WARNING and ERROR info)
=============================================

The status icon is the icon on the right side of the job. It tells you if the job is a new, queued, running, terminated, ready, ready with a warning, or ready with an error condition. 

The warning and error condition is determined from the logfile of the job. If it contains a WARNING, the icon will display a warning triangle. If the logfile contains ERROR, the status icon will change into a red stop sign. If the standard error output of a job contains unexpected information this will also be reported as an ERROR. 

The details of the error or warning will be shown in a color just below the job. Obviously, when a job has ended with an error you will normally not have useful results. If a warning has been printed, you should make sure you understand the warning, and that the ADF did perform the calculation that you intended. 

Selecting Jobs
==============

You can select one or more jobs with: 

- left click - select that job

- shift left click - select a range of jobs

- right click (or control left click) - toggle that job to be selected or not selected

- click on the search icon - clear the selection

To clear the selection, press the ESC key, use the **Job → Clear Selection** menu command, or click somewhere in white space on the bottom or in the selected job (thus not on the name, queue, or one of the icons). 

Running a job: .run and .job
============================

When saving your job, AMSinput saves a .ams file and a .run file. The .ams file contains all information for AMSinput,  and if you wish to make changes to your job use AMSinput to make them. AMSinput will read the .ams file. 

The .run file contains the basic commands and input to run your calculation. It is intentionally kept as simple as possible. 

However, typically some more administrative things need to be done: make empty working directories, make some links to follow a running calculation, etc. This used to be done by the run script, but not any more. If you wish to use the run script yourself you are responsible of taking care of such details. 

To run your calculation, use the Run command from the File menu. This will tell AMSjobs to run your job. Alternatively, you can switch to AMSjobs, select your job (that you should have saved from AMSinput), and select Run from AMSjobs Job menu. 

AMSjobs will create the real job script (with .job extension). This is a the .run script as saved by AMSinput, with the administrative things included at the front and at the end. 

**As the .run script is simply included, you may edit it if you wish, and AMSjobs will automatically include your changed .run script.** 

If the environment variable SCM_RESULTDIR has been set, the job script will change into that directory. Next it will run from there, and all result files will be stored in that directory. 

If the environment variable SCM_RESULTDIR has not been set, the job script will execute in the directory where it is located, and the result files will also be located in that place. 

The exact command given to run the job depends on the queue configuration. 

Job files
=========

Local files
-----------

The local files section lists all files that AMSjobs found. They all have the same name (the name of the job), and different extensions. Here you can see what files belong to a job, including modification date and time, and the size of the files. 

Double clicking on some of the extensions will open that file. For example, double clicking a .ams file will open it in AMSinput. Double clicking a KF results file will open it in the KFbrowser. 

One useful application is double click on the .run file. This will open the .run file in a text editor, depending on your operating system. In this editor you can actually make changes to the .run file. When you save it this modified run file will be used when you run the job. The .job file will be overwritten, thus you need to change the .run file if you wish to make manual changes. 

You can also first select a local file. Next select one of the GUI modules from the SCM menu, and the selected file will be opened by that GUI module, if possible. 

Within the local files you may also find a directory called 'results'. This will be created when result files are present other then the standard result files. For local jobs they will always be present, for remote jobs it will be created when using the Transfer from Remote command or when you click on one of the remote files in the remote .results folder,  as displayed in AMSjobs. 

You can select multiple files using click followed by shift-click (for a range), or using control-click to add the clicked file to the selection.
Once multiple files are selected, you can open all of them at the same time via the SCM menu (either from the menu or via a right-click in the selection).
Alternatively, you can use the Backspace or Job->Delete menu command to delete the selected files.

Remote files
------------

This is a similar list of files as the local files list, but these files reside on a the remote machine as specified in the job details. If you are preparing a new calculation it will be empty. When a calculation is complete, it will show all the result files on the remote machine. 

At the top of the list the name of the directory in which the files live on the remote machine is shown. 

You can select a remote file by clicking on it. This will cause the file to be transferred to the local machine, replacing any local file with the same name. If you click on any of the remote files in the .results directory all remote files  belonging to the job will be transferred (overwriting local files with the same names). 

After selecting the remote file it will be used by GUI modules started from the SCM menu. 

Clean Up
========

After a calculation many files may be saved. Some of them might not be of interest for you, or only temporarily. You can use the **Job → Clean Up** command to remove files no longer needed. It will present a dialog where you can select exactly what files to remove. The most important result files will by default be saved. 

Note that you can also just select the files you want to delete and press backspace.

Archive jobs
============

You can use the **Job → Archive** command to collect most files belonging to a job and put them in a gzipped tar archive. This will significantly reduce the amount of space used by the job. The command will operate on all selected jobs. 

If you use an archived job in AMSjobs (or any GUI module) will recognize it as archived, and automatically unarchive it before using. So in practice you can just archive many (or all) of your jobs and forget about it. This will save a lot of disk space. 

Import / Export jobs
====================

If you want to share jobs with other users (or SCM support) there is an easy way to do this. Just select your job in AMSjobs,  and use the **Job → Export...** command. A dialog will appear that allows you to specify where to save the packaged job. The packaged job is in principle just a gzipped tar file containing all job files, with some extra data so that AMSjobs recognizes it as a packaged job. 

Use the **Job → Import...** command to open such a packaged job and add it to your AMSjobs listing. 

Find job files
==============

After some time you may have a lot of result files collected in the same folder. The **Job → Show Files** command will show the files belonging to the selected job on your computer. How it does this exactly depends on your operating system. Typically a window will open showing the files in the directory, with the files of the job selected. 

Test Job
========

When you have trouble running jobs, either locally or via some queue you have defined, it is sometimes not easy to figure out what the problem is. To help you (or us, when you ask for support) diagnose the problem AMSjobs can make a test job. 

Use the **Job → Generate Test Job**, select it in your AMSjobs window, assign the queue you want to use (or skip this step if you want to test the default queue), and use the **Job → Run** command. 

The logfile of that job will contain a lot of diagnostic information, like the environment, license details, adf version details and more. Some consistency checks are performed. This information might help you to solve the problem. If not,  contact us, explain the problem and include the output of the test job. 

Queues
******

A queue tells AMSjobs how to run the selected job: where (possibly on a remote system!), how and by whom. 

In the Queue menu you see a list of queues. Select one of them to use that queue when running the selected jobs. 

If you have configured queues for remote machines, you will be able to use those remote machines just as easily as your local machine. AMSjobs will take care of copying files to and from the remote machine. It will also start or submit your job, and inform you of the progress of your job. 

If you have defined your own queue, for example to run on some remote cluster, you can make that the default queue (instead of the Sequential queue) by using the **Queue → Set Default** menu command. 

For each job, you can specify some extra text in the options field next to the name of the queue (with the gray rectangle around it). How this text is used depends on how your queues are set up. For example, the Interactive queue uses it to specify the number of tasks to use in your job. For batch systems, it might be the number of nodes to use, or some time limit or batch queue name. 

When starting AMSjobs the first time, you will see the Interactive and the Sequential queue. Both will run jobs on your local machine, using as many tasks as possible. You can enter a number in the options field of the job (with the gray rectangle) to set the number of tasks use explicitly. 

Via the GUI Preferences, you can also configure AMSjobs to automatically pick up queues stored in a central location. They need to be defined once, and any AMSjobs user can import them. Such queues are called 'Dynamic queues'.  

.. warning::

  The ``Job status command`` in default queues have been updated, to avoid excess load on the batch system. 

  For PBS the qstat command has been changed into qstat $jid. And a similar change for the other batch systems, the syntax depends on your batch sytem.

  You may want to change your own queue in the same way.



Interactive Queue
=================

When you run AMSjobs for the first time, it will make sure that an Interactive queue exists. If not, it will automatically create such a queue for you. 

When you use the interactive queue to run a job, your job will run immediately on the local machine. Thus you can run many jobs at the same time. 

To specify how many tasks to use, enter a number in the options field. If you leave it empty all cores will be used. 

As you could be overloading your machine it may not be what you want, but it is great if you have some job running and want another small on to run at the same time. Another use would be to run several single-core jobs on a multi-core desktop machine at the same time. 

Sequential Queue
================

When you run AMSjobs for the first time, it will also make sure that a Sequential queue exists. If not, it will automatically create such a queue for you. 

When you use the Sequential queue to run a job, your job will run interactively on the local machine as soon as no other job is running. Thus you can give the run command in AMSjobs for many jobs at the same time, but they will actually run one after the other. 

To specify how many tasks to use, enter a number in the options field. If you leave it empty all cores will be used. 

Normally, this is the most convenient and efficient way to run jobs on your local machine. For that reason it is the default queue (unless you change that). 

Setting up your own Queues
==========================

.. _metatag QUEUES: 

You can define a queue in several ways: 

+ **Queue → New...** based on one of the included example queues,

+ **Queue → Edit...** change details of a queue (or make a new one if you change the queue name as well),

+ **SCM → Preferences → AMSjobs → Dynamic Queues** import queues stored on some central system

When using the **Queue → New...**  command, you can select what configuration to start with: 

+ Interactive: make a new Interactive queue. For example, to make a special version that will force your job to use only 1 task.

+ LSF, PBS, SGE: make a new queue that will submit your job to the selected batch system. The configuration of these batch systems can be quite different. The included examples should server as an example only, you will need to fix the details. In the included examples the options field is used to specify the number of nodes to be used.

When using the **Queue → Edit...**  command, you select what queue configuration to edit. 

Using either of these commands, a dialog will appear requesting you to set the details of the queue you are creating (or modifying). 

Often it requires some experimentation to set up all the details correctly. You can use the **Help → Trace Commands To Remote** menu  command in AMSjobs to trace the commands given to communicate with the remote host (typically the ssh or putty command with arguments),  and to see the responses to these commands received from the remote host. This trace will be shown in via AMStail. 

The following details may be set when configuring a queue: 

``Remote host``
   Name of the machine on which you wish to issue the command to run (or submit) your job.  You should be able to connect to that machine using ssh, and the host name as specified here.  If you wish to run on your local machine, leave this field empty or specify localhost. 

``Remote user``
   The username that you need to specify in the ssh command, if any. Typically, this is your username on the remote machine. If you have configured ssh to log in on your remote machine without specifying a user name, you can just leave this field empty. That is also the most convenient way to set up a queue that is to be used by other people as well (with their own accounts on the remote machine). 

``Path to private ssh key``
   The path to the private ssh key for this remote machine. If it is an absolute path it will be used as is, otherwise it will be relative to the home directory. The default is empty, in which case the default ssh key will be used (possibly defined in your .ssh/config file).

``Remote job directory``
   On the remote machine, AMSjobs needs to set up your input files and run script, and needs to collect the results. For that purpose AMSjobs will make its own directories within the directory you specify. A typical value would be something like $HOME/jobs. 

``Run command``
   The command **on the remote host** to be executed. AMSjobs will always first ssh into the Remote machine, and  then issue the Run command. The run command should start the job interactively, or submit the job using some batch system.  If the remote host field is empty or localhost, the run command will be executed on the local machine. 

   $job will be replaced by the full path to your job script on the remote machine. 

   $jobname will be replaced by a jobname based on the value of $job, but truncated and with spaces removed. 

   $options will be replaced by the contents of the Options field.   The Options typically will be used to specify the number of tasks, a time limit, or a batch queue name.  

   If you use the run command to submit a job to some batch system, it should return a number. This number will be assigned to $jid, and may be used by the kill and job status commands. 

   To run interactively, just enter "sh $job". To submit your job to a  queue, specify the submit command (for example, qsub, or some other special submit tool). For example, check the pre-configured queues for Interactive and batch systems (via the **Queue → New...** menu command). 

   The job script that is automatically generated accepts an optional parameter. This parameter is 'eval-ed' at the start of the script. Thus, you can use it to set environment variables (like NSCM) or other things. 

   When the run command is issued, the working directory will be $SCM_RESULTDIR or the location of the .job script if no SCM_RESULTDIR has been defined. The results (output file and so on) will also be saved in that location.  Note that the computational engines (ADF, BAND, ...) will automatically change their working directory when started to $SCM_TMPDIR. You should make sure that SCM_TMPDIR points to the proper location as you want to make sure you are writing to a fast local disk, and not to the (typically shared) disk where the results are stored. 

``Use Local Batch``
   If yes, jobs will be queued on the local machine. Only one job will be running at a time. This is set for the Sequential queue (which is default). Currently this value is ignored when the job will be queued or run on a remote system or using a cloud machine. 

``Kill command``
   The command to use to kill a queued or running job. In this command $jid will be replaced by the job id (from the output of the run command), or by the process id. For interactive jobs, killall $pid should work fine. This killall is actually replaced by a special script that takes care to kill adf and all child processes. 

``Job status command``
   This command will be used to determine if a job is still queued or running. If a job is no longer queued or running, it should return an empty string. Anything else will server as indication that the job is alive. 

   For interactive jobs ps -p $pid | grep $pid works fine. 
   
   For batch jobs the command typically is qstat $jid | grep -w $pid 
   (note: the $jid after the qstat was added recently, and the exact syntax depends on your batch system).

   The job status command is issued every 5 minutes by default, per job, while the job is running or queued.
   You can change that by setting the SCM_STATUSINTERVAL environment variable on the remote machine (where the batch commands are executed).

``System status command``
   The command to use to determine the system status. This might be uptime, or some qstat command for batch systems. 

``Prolog command``
   The command to execute by the job script, just before the included .run script. This will be used to set up the environment properly. For example, you would source a script file to set all environment variables for ADF like AMSHOME, AMSBIN etc. This is especially important if you are working with different versions of ADF at the same time. Note that the job script is started using /bin/sh, so you should use sh-like syntax (an not csh-like). If your environment is already set up correctly for running ADF on the remote host, without issuing any commands, you can leave this field empty. 

   In your prolog command you can use environment variables that are defined by the job script. Most importantly,  the environment variable SCM_OUT points to the output file of the job, SCM_LOG points to the logfile, and SCM_ERR points to the  error output. This makes it easy to print some additional information to those files. 

   You can put multiple commands here separated by ";". However, in most cases it is easier to source a file with commands. By sourcing it you make sure that changes in the environment defined in the sourced file will also be available by the job script. 

``Epilog command``
   This is the command to run by the job script, just after the included .run script. You can use it to copy save result files, or to perform some cleanup action. Again, use sh-style syntax, and the same environment variables are still defined.. 

``Copy results back``
   If this field is set to 'yes', all result files from this job will be copied back to the local machine automatically when the job is ready (only for remote jobs). 

``Cloud init``
   When this field is not empty, it will be used to initialize a cloud machine, if needed. A typical value for AWS machines would be 'AWSInit adf2019.204 t2.micro laptop'. Check the Cloud computing description for details.


Cloud computing
===============

You can use AMSjobs to run jobs on machines that are in the cloud. Currently the Amazon Elastic Cloud is supported (AWS EC2).

To use AWS:

1. Create an AWS account or ask the person responsible for managing your organization's AWS account to create an IAM user for you. Log in to the AWS Console using the credentials and go through the following steps:

a. Generate an ssh key pair: in the left column AWS EC2 Dashboard you will find 'Key Pairs' in the 'Network & Security' section. Click on that, and next on the 'Create Key Pair' button on the top. Enter a name without spaces, for example ``aws_ssh_key``, and the newly generated private key will be saved on your computer. Move it to a safe location (like your .ssh folder). Make sure others have no permissions to read/write/execute that file.

b. Modify the default security group that will be used for each new instance, to allow inbound ssh connections from your IP address (or an address range). You can also restrict the outbound traffic but you need to make sure that the communication to SCM license servers (license.scm.com, license1.scm.com, license2.scm.com) on the https port (443) is not blocked. The security groups are found under 'Network & Security' in the EC2 Dashboard.

c. Create an AWS access key for the command-line interface: click 'My Security Credentials' in the account drop-down menu, press the 'Create access key' button under 'Access keys for CLI, SDK, & API access', store the key ID and the secret in a safe place. You can create extra keys at any time.


2. Install AWS CLI (the AWS command line interface). 

For instructions check the `Amazon AWS CLI <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html>`__ documentation.
Make sure you can use the AWS CLI as a normal user (try ``aws --version`` in a terminal window).

For example, on a mac 

::

   sudo chmod -r ugo+rX /usr/local/aws/
   sudo chmod -r ugo+rX /usr/local/bin/aws

is needed at the time this documentation was written.

3. Configure the AWS CLI by running ``aws configure``. Enter the access key ID, the corresponding secret and the AWS region when prompted. The default output format does not matter so you can leave it at the default.

4. Have a look at AMIs (Amazon Machine Images) available to you, by name or by ID.  You need to know which AMI to use for your cloud instance. Pre-existing AMIs can be found under 'Images' on the EC2 Dashboard. You can, for example, search by name. 

Optionally, you can also create your own AMI containing ADF from one of the standard Linux images provided by Amazon: 

- Start a Linux instance, 
- Copy an ADF archive and unpack it in the home directory of the default user, 
- Edit ~/.bashrc and add the following command at the top of the file, for example for ADF installed in ~/adf2019.301:

::

   source $HOME/adf2019.301/amsbashrc.sh

- Install the task spooler tsp. This is used by the default AWS queue in AMSjobs to get jobs to run in sequential mode (one after another):

::

   sudo apt install task-spooler


5. In AMSjobs on your local computer make a new AWS queue.

The easy way to set up an AWS queue is to base it on the AWS example queue included in AMSjobs (use the **New...** command from the **Queue** menu).
Make sure to change the ssh_key_name and the SCM cloud credentials.

In general the following queue options are relevant for AWS queues:

``Queue name``
   'AWS' (or something like that, it's up to you)

``Cloud init``
  Specify how to initialize cloud instances. Currently only AWS is supported, for which you need to use AWSinit.
   
  For example ``AWSInit adf2019.204 t2.micro aws_ssh_key``

  ``AWSInit image-name instance-type key-name [--size size]``
     AWSInit manages AWS cloud instances. It starts new cloud instances when needed, or reuses previously started cloud instances if all arguments are identical.
     It will take care to pass the IP and username that should be used with the new cloud instance to AMSjobs. The hostname field of the queue is ignored, 
     the username field of the queue is used and can be used to override the username returned by ASWInit. Currently ASWInit always returns ubuntu as username.

  image-name
     The name of an AMI image (optionally using wildcards), or the id of an AMI image. 
     If multiple images match the one with the latest creation date will be used. 
     The search is for AMI images owned by you (self) or by SCM.
     You can use wildcards to get the latest adf versions: ``adf*`` to get the latest, or ``adf2019.2*`` to get the latest adf2019.2xx
  
  instance-type
     The instance-type to use (see the AWS documentation.
     Note you may use $options in the AWSinit line to specify the actual instance-type
  
  key-name
     The name of your key as known by AWS (should have been created in step 1a)
  
  size (optional) 
     the size of the disk space in GB

``Copy results back`` 
   yes

   **Be sure to set this to yes**, otherwise your results are gone once the cloud instance is terminated

``Path to private ssh key``
   Set it to the path of the private key you saved in step 1a.


AMSjobs will automatically start an AWS cloud instance if needed. 
If a cloud machine using the same AWSInit command (with $options replaced by the actual value) is already running it will be reused. 
Once it is ready the job will be started on that cloud machine, and from this point it is just like any other remote machine.
If you do not want to reuse an already running cloud instance you need to make a new queue, with a different Cloud init command.
For example, use a different image-name (which actually may be the same image), or add a -size option.

Starting an AWS cloud instance may take a while. AMSjobs will be waiting for it, and show this using a progress dialog.
You can click the **Dismiss** button which will stop the submission of the job. It will NOT cancel the starting of the cloud instance.
So you can use the Run command again at a later time and AMSjobs will automatically pick up this same instance (either use it or 
continue to wait for it).

Once you are done with this remote machine do not forget to terminate the cloud instance.
You can do this via the AWS web interface.
Alternatively, when you Quit AMSjobs it will propose to terminate the running cloud instances, if it can find any.

Obviously terminating cloud instances while they are being used is not a good idea. The GUI will run into lots of TIMEOUTS as 
it cannot reach the cloud instance any more, while it expects it to be alive. So before terminating a cloud instance make sure 
you have no jobs running that are using it.


Dynamic queues
==============

Dynamic queues are updated automatically when AMSjobs starts. 

AMSjobs will check with the hosts that you have specified in the Preferences: 

::

   Open GUI preferences: SCM → Preferences
   Panel bar Module → AMSjobs
   Click the + button in front of Dynamic Queues
   Enter the host name of the host on which to look for dynamic queues
   Optionally: enter the username of the remote machine on which to look for dynamic queues
   Click the 'Save' button at the bottom of the panel, and restart AMSjobs

If the username is left empty (or to the value (username)), no username will be used when connecting to the remote machine. Then your ssh configuration determines what username to use. 

On the remote hosts listed, AMSjobs first checks the $SCM_QUEUES environment variable. If it is set, it will import the queues defined in the $SCM_QUEUES directory. If it is not defined it will try to import queues from $HOME/.scm_gui. This is the location where AMSjobs stores the queue information. 

To define the dynamic queues, first figure out what queue settings you (and/or others) want to use.  You can do this by configuring a normal queue with AMSjobs as described. As dynamic queues typically will be used by  many users, you should not specify a username (unless you want all users to use the same account on some system).  Make sure it works properly. 

Next make a directory on the remote system where you want to store the dynamic queue definitions. 

Set the SCM_QUEUES environment variable system wide on remote system for all users. If SCM_QUEUES is not defined, AMSjobs will search the $HOME/.scmgui directory on the remote platform.  This way users can set up their own dynamic queues. 

Locate the files that define your queue: you can find these files in the $HOME/.scm_gui directory. They have the name of the queue, with a .tid extension, and are plain text files. Next, copy these files into the $SCM_QUEUES directory on the remote system. Make sure all users have permissions to read the $SCM_QUEUES directory and the files in it. 

Note: the server that stores the dynamic queues need not be the same machine on which the jobs will run. 

Note: the AMSjobs user needs to have access to the server via ssh 

Example Queue configurations for SGE and PBS
============================================

Here you will find example .tid files for SGE and PBS. They will not work without change, you need to set at least the proper hostname and runcmd, and most likely the prolog needs to be changed (or  just made empty). 

The contents of the .tid file for a SGE queue might look something like this: 

::

   # hostname: machine.domain
   # username:
   # jobscript:
   # prolog: source $HOME/setup/adf2017
   # epilog:
   # jobdir: $HOME/jobs
   # runcmd: qsub -pe s3_mpich $options -q short3.q "$job"
   # batch: no
   # options: 2-2
   # killcmd: qdel $jid
   # jobstatuscmd: qstat | grep " $jid "
   # sysstatuscmd: qstat
   # label: My SGE queue
   # logfile: logfile

Similar, for a PBS queue it might look something like this: 

::

   # hostname: machine.domain
   # username:
   # jobscript:
   # prolog: source $HOME/setup/adf2017
   # epilog:
   # jobdir: $HOME/jobs
   # runcmd: qsub -lnodes=2:ppn=2:infiniband -lwalltime=$options "$job"
   # batch: no
   # options: 0:15:00
   # killcmd: qdel $jid
   # jobstatuscmd: qstat | grep $jid
   # sysstatuscmd: qstat -q
   # label: My PBS queue
   # logfile: logfile

Tools: set up many jobs and collect data from many jobs 
********************************************************

.. _metatag SCRIPTING: 

You can use the Prepare tool to set up batches of jobs. For example, first set up an ADF calculation with your preferred basis set, XC potential and so on using AMSinput. Next, use the Prepare tool to generate a batch of similar jobs, but for different molecules (taken from .xyz files for example). Or you could set up a calculation for your molecule, and generate a set of jobs with different XC potentials and / or integration accuracies. 

The Reporting tool is to generate a report of one or more calculations. This report will contain the information that you select when you define a 'report template'. Most of the properties that have been saved to .t21 will be available. And you can generate images as will (like HOMO or SCF density). These results will typically be collected in an HTML table: one row for each molecule, and one columns for each property. 

A report template defines what information to put into the report. 

Prepare: set up many jobs at once
=================================

You activate the Prepare tool via the **Tools → Prepare...** menu command. 

A window will appear that you can use to specify how to generate a set of jobs. 

Three main list fields are presented: the Run field, the coordinates field, and the input options field. In each of these lists you can specify multiple options. When pressing 'OK' AMSjobs will generate the jobs by combining the options in all possible ways. 

**Run list**
Select one or more .ams files to run. A .ams file is just a calculation that has been set up using AMSinput before. Alternatively, one may use one of the predefined .ams files as present in the pull-down menu when you press the '+' button. To add a .ams file, use the pull-down menu, or specify a file name in the text field and press return. You may use wild card in the text field, so the default value (\*.ams) will expand to all .ams files in the current directory. To remove something from the list, select it and press the '-' button. 

**Coordinates list**
When this list is empty, the molecule as found in the .ams files will be used. When one or more sets of coordinates is present in this list, the molecule in the .ams file(s) will be replaced by the molecules as defined in the coordinate files. You may use .ams files, .xyz files, .t21 results files, .mol files, .pdb files or whatever other format AMSinput can use with the 'Import Coordinates' function. By listing multiple files here your .ams files (that you listed in the Run: list box) will all be executed with each of the molecules in turn. Thus, if you specified two run files (for example a Single Point calculation, and a Geometry Optimization), and three molecules, you will end up with 6 jobs. 

**Input options list**
In this list you may define alternative input options. The corresponding input options in the .ams file will be replaced by the values that you specify here. So if you specify two different basis sets, each job will be replaced by two new jobs, one with each basis set that you specify. You may also specify other things, like integration accuracy and so on. If you specify only one value, that value will be used in all jobs. If you specify multiple values (by repeatedly adding the option) you will generated multiple jobs. 

The text field may be used to add additional keywords, or replace existing ones, with the value specified. These options will be added to the list of options by pressing return in the text field. The values will be used as the '-k' argument to the amsprep command. For detailed information about this please check the amsprep documentation. 

**Produce jobs options**
The final fields will tell the prepare tool where to generate the jobs (the directory is relative to the current directory, and will be created if it does not yet exists). Also one big job will be created that is just a concatenation of all the individual jobs. When running interactively it might be more convenient to run this job instead of all the individual jobs. The results should be identical, the big job will produce files that look as if they have been produced by the individual jobs. 

Report: collect data from many jobs
===================================

To make a report of calculation results, you first have to set up a 'Report Template' that defines what information should be collected for the report. You manage these report templates via the New, Edit and Delete Report Template menu commands in the Tools menu. 

When editing a report template, a dialog box will appear with many options. Just check the options for the information that you wish to collect in your report. Note that you can also include images (of orbitals, and so on) in the report. 

If you wish to include something that is not present in the dialog, you can use the last field: Extra AMSreport command line options. Whatever you specify here will be passed to AMSreport to generate the report. This allows you to get any information that is available on a .t21 result file into your report. Check the AMSreport documentation for syntax details. 

Once you have your Report template set up, you can use the Build command to actually generate a report. The data for the  report will be taken from the currently selected jobs. You can update the report with new data from other jobs by using  the Update Last Report command, with one or more different jobs selected. These jobs may even be located in a different directory. This allows you to collect information from jobs a few at a time. 


Series of jobs depending on each other
**************************************

In AMSinput you can specify (in the Coordinates panel) that it should use the molecule from some other file or job.
Then a job is created that depends on another job or on some other file (for example a .sdf file).

AMSjobs shows such dependencies when you select a job.

To run such a series of jobs that depend upon each other, you can just run the last job in the series.
AMSjobs will determine what other jobs need to be run as well, and automatically start them (using the same Queue as the job you started yourself).

In the Tutorials you will find several examples of such jobs.

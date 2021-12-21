Background processes with no interface
######################################

scmd: communication between GUI modules
***************************************

The scmd process should always be running when any of the GUI modules is active. You should have one scmd process (per user, if you are working with multiple users). The scmd process has no window, it should normally be invisible to the user. 

The purpose of the scmd process is to handle all communication between GUI modules. For example, if you use the SCM menu to start a GUI module, that command is actually handled by the scmd process. It will figure out if a new module needs to be started, or if an already open module with that particular job should be activated. 

Starting jobs, and handling the local Sequential queue is also done by scmd. 

Communication between the GUI modules and scmd is done using TCP/IP within the local machine. If such communications are blocked, for example by a firewall, this will make the GUI non-functional! So in case of trouble, make sure you are not blocking TCP/IP traffic within the local machine. The GUI will never accept any TCP/IP connection from outside, only from within the local machine. 

scmjobd: monitor running jobs
*****************************

The scmjobd processes are also faceless background processes that belong to the GUI. They are started and terminated as needed, normally one per queued or running job. Their task is to monitor the progress of jobs, updating the status if it changes, getting logfile results for remote jobs, and killing jobs (if you use the Kill command in AMSjobs). Even if all windows of the GUI are closed they may still continue to be present if you have queued or running jobs. 

The scmjobd processes communicate with the other GUI components using TCP/IP, via the scmd process. To monitor remote jobs they will use ssh to connect to the remote machines. 


SCM menu
########

All GUI modules have an SCM menu. The SCM menu is the leftmost menu in all modules, and is represented by either the SCM-logo or the text SCM. 

In general, when you select a command from the SCM menu you will switch to the selected module, showing the same job as you have open in the current module. If such a module is already running with that particular job open, it will be brought to the front. If you use the SCM menu to open the same module as is currently active, it will start another blank copy of this module. Thus the SCM menu is very convenient to quickly switch between the already open windows belonging to the same job. 

As a shortcut you can also right-click on a job name in AMSjobs, and the SCM menu will appear with the job you clicked on selected.

In AMSjobs the currently selected job will be used with the SCM menu. Thus, if you have one job selected, using the **SCM → View** command will start or switch to AMSview, showing the results of the selected job. If you have no job selected, or more then one, the selected module will start blank. 

One important exception within AMSjobs: the Input module will always start a new blank version. If you wish to show the input GUI for the selected job you need to click in the icon in front of it (reading 'ADF', 'BAND', or some other job type). 

The SCM menu also allows you access to preferences for that are used by all GUI modules: **SCM → Preferences**

In some cases a GUI module is able to open several file types. For example, AMSmovie can open the logfile or the .t21 file of a calculation. By selecting a file in AMSjobs (after opening the job by clicking on the triangle) you can force AMSmovie to open the .t21 or the .logfile. In a similar way, you can force AMSview to open a .t21 or a .t41 file.   

The **SCM → Quit** and **SCM → Quit All** menu commands will close windows: the Quit command will close all windows belonging to the current job, the Quit All command will close all open GUI windows, as well as any invisible background processes belonging to the GUI (scmd and scmjobd).    

GUI Environment Variables
#########################

As of the 2016.102 version, if you start the MacOSX ADF-GUI application the environment defined by your shell startup scripts is ignored.
Instead the bundled ADF is used, and environment variables may be defined in a file $HOME/.scmenv and/or /Libary/Application Support/SCM/scmenv.

In the following list the environment variables that are specific for the ADF-GUI are listed  (the normal environment variables like AMSHOME, AMSBIN and SCMLICENSE are also used by the ADF-GUI):

**BROWSER**: Fallback for **SCM_BROWSER**: the HTML browser used for both local and remote documents (not for Windows or Mac). Default value: none (the PATH will be searched).

**DISPLAY**: X-window display to use, when using ssh normally you should NOT set it manually. It is required (for all X11 programs) except on Windows.

**PSEUDO_DIR**: Path to the folder containing Quantum ESPRESSO pseudo potential files. If not set, a :ref:`standard search path <metatag QESETUP>` is used.

**SCM_ADFCRSDIR**: Path to the folder containing the ADFCRS-2018 database, if different from the default set by AMSpackages.

**SCM_AMSREPORT_PLAIN**: No labels or units in amsreport output. Not set by default.

**SCM_BROWSER**: The HTML browser used for both local and remote documents (not for Windows or Mac). Default value: none (the PATH will be searched).

**SCM_DEBUG**: Turn on many debug items in ADF and avoid clean-up by GUI. Not set by default.

**SCM_DEBUG_SSH**: Set to yes to debug communication issues: all non-multiplexed  ssh commands will be printed to stderr. Set to all to see all SSH commands, even if multiplexed. Not set by default.

**SCM_DEFAULT_DIALOG**: Set to 1 to get the original file dialogs back on Linux. Not set by default.

**SCM_ERROR_MAIL**: E-mail address for error reports. Default value: errors@scm.com.

**SCM_DOCINDEXDIR**: Location of the directory in which the index for the documentation will be stored. Setting it makes it possible to share this index and save some space. Default value: $HOME/.scm_gui/doc.index.

**SCM_FFMPEG**: The ffmpeg program to use to generate movies. Default value: none (the PATH will be searched).

**SCM_FFMPEG_ARGS**: The arguments to pass to ffmpeg. Default value: none. The -i and -t (for looping movies) will always be added automatically.

**SCM_GEOMODSBYSIZE**: The geometry slider will always move the smallest group of atoms. Default value: none (the last selected atoms will move).

**SCM_GUIRC**: Location of the preferences file. Default value: $HOME/.scm_guirc.

**SCM_GUIPREFSDIR**: Location of the preferences directory. Default value: $HOME/.scm_gui.

**SCM_SCMJOBD_RESTART**: Force a restart of the scmjobd job monitors every this many milliseconds. Not set by default (600000 which is every 10 minutes).

**SCM_KEEPJOB**: Do not remove the .job files automatically

**SCM_KFBROWSER_EXPERT**: Define it to make the expert mode in the KFbrowser the default. The non-expert mode will be the default mode.

**SCM_LFDFT**: Path to the folder containing the LFDFT datatbase, if different from the default set by AMSpackages.

**SCM_LOG**: Set to the full path of a file to log some stuff the GUI does (mainly invocation of other modules/programs). Not set by default.

**SCM_LOG_SCMJOBD**: Set to the full path of a file to log some what scmjobd is doing. Not set by default.

**SCM_NO_RSYNC**: do not use rsync to transfer files to/from remote machines, but use the previous implementation (with tar/gz). Not set by default.

**SCM_NO_LOGIN_SHELL_FOR_MONITOR**: the scripts to monitor a running job normally run in a new login shell. Setting this env var will not force a login shell. Note it must be set on the machine where the monitor script is running, and you need to make sure that the queue commands (as defined in the AMSjobs queues) will work properly.

**SCM_NO_SSH_MULTIPLEXING**: If set SSH multiplexing (bundle multiple ssh connections in one) will be avoided. Not set by default.

**SCM_OFFSCREEN**: Set it to some value to force the GUI modules to run offscreen. Used for testing.

**SCM_OLD_TRANSFERS**: If set files are transferred one by one instead of in a tar archive (turn on when you run into tar compatibility issues). Not set by default.

**SCM_OPENGL_SOFTWARE**: Force software rendering, this often prevents problems with remote GUI use or incompatible graphics cards. It is significantly slower. Not set by default.

**SCM_PACKMOL**: The packmol program to used by the Builder. Default value: none (the PATH will be searched).

**SCM_RESULTDIR**: Location of the results directory. Default value: none (directory where the .ams files etc live is used).

**SCM_STRUCTURES**: Location of the structures directory. Default value: none.

**SCM_TITLEVERSION**: Show SVN revision number in title. Not set by default (show only version number).

**SCM_TMPDIR**: Temporary files will be made in this directory (should exists if set). Default value, if not set $TMPDIR $TMP /tmp $HOME or the current directory is used (in that order).

**SCM_TPLDIR**: Location of the presets directory. Default value: none.

**SCM_STATUSINTERVAL**: The time in seconds between the job status commands used to detect killed jobs (like qstat). Default value: 600.

**SCM_QUEUES**: Path to the dynamic queues directory. Default value: none (AMSjobs will search the remote $HOME/.scmgui).

**SCM_QEDIR**: Path to the folder containing Quantum ESPRESSO installation (binaries and pseudo potentials). Set it to force the installation of QE somewhere outside your $AMSHOME. If not set, a :ref:`standard search path <metatag QESETUP>` is used.

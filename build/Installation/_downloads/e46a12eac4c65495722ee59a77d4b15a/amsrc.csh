#!/bin/csh
# This file should be sourced by a c-shell (csh) or tc-shell (tcsh) shell. 
# For more information about this file, please read:
# - https://www.scm.com/doc/Installation/Installation.html
# - https://www.scm.com/doc/Installation/Appendix_A_Environment_Variables.html

################################################################################
# Change the following variables to the corresponding locations on the system! #
################################################################################

# AMSHOME refers to the folder that contains the folders "bin", "atomicdata", "scripting" and a few others
setenv AMSHOME $HOME/ams2021.207
# SCM_TMPDIR is used for writing temporary data during calculations. For best performance, this needs to be fast&local storage (no network mount).
setenv SCM_TMPDIR /tmp
# SCMLICENSE should point to your license file. Make sure this location has write permissions when using autolicense
setenv SCMLICENSE "$AMSHOME"/license.txt
# SCM_PYTHONDIR should point to the location where you want the SCM python stack to set up the virtual environment. 
# This is for installing additional python packages from PyPi with "amspython -m pip install"
setenv SCM_PYTHONDIR=$HOME/.scm/python

# Variables below this line usually do not need to be changed
setenv AMSBIN "$AMSHOME"/bin
setenv AMSRESOURCES "$AMSHOME"/atomicdata

# add $AMSBIN to the PATH
set path=($AMSBIN $path)

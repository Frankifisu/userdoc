#!/usr/bin/python

import os
import argparse
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', help="input file", dest='inputfile', required=True)
parser.add_argument('--output', '-o', help="output file", dest='outputfile', required=True)
parser.add_argument('--trunk', help="toggle for the trunk version", dest='trunk', default=False, action="store_true")

options = parser.parse_args()

try:
	infile = open(options.inputfile, 'r')
	intext = infile.read()
	infile.close()
except:
	"failed to read the input file!"
	traceback.print_exc()

# remove the ======= line
intext = re.sub(r'=*', r'', intext, flags=re.IGNORECASE|re.MULTILINE)
# remove manual line breaks
intext = re.sub(r'\n[ ]{8,24}', ' ', intext, flags=re.IGNORECASE|re.MULTILINE)
# change indentation to 3 spaces
intext = re.sub(r'    ', '   ', intext, flags=re.IGNORECASE|re.MULTILINE)
# remove the commented lines at the end
intext = re.sub(r'#.*\n','', intext, flags=re.IGNORECASE|re.MULTILINE)
# If The first author has a first letter followed by a dot and a space, Sphinx will turn that into a list. Escape the space to solve it
intext = re.sub(r'(-\n[A-Z]\.) ',r'\1\\ ', intext, flags=re.IGNORECASE|re.MULTILINE)
intext = re.sub(r'(\n   - [A-Z]\.) ',r'\1\\ ', intext, flags=re.IGNORECASE|re.MULTILINE)



regex=r'\n(.*?)\n[-]+\n(.*?)\n[ ]*(.*?)\n[ ]*(.*?)\n[ ]*(http.*?)\n((?:[ ]*- .*\n)*)\n'

outtext = re.sub(regex, r'\n\1\n   \2 *\3* `\4 <\5>`__\n\n\6\n', intext)

if options.trunk:
    header="""Included force fields (development)
##############################################

.. _forcefields_development: 

See also `Included force fields (released version) <Included_Forcefields.html>`__


"""
else:
    header="""Included force fields
############################

.. _forcefields: 

See also `Included force fields (development version) <Included_Forcefields_Trunk.html>`__


"""

outtext= header + outtext
outfile = open(options.outputfile, 'w')
outfile.write(outtext)
outfile.close

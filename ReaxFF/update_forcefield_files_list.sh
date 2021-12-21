#!/bin/sh

# ##################################
# Create the reaxff forcefield pages
# ##################################
# see get the svn repo url, because we might need a specific username
svnurl=`svn info | grep "^URL" | cut -d ' ' -f 2| sed 's#userdoc/##' | sed 's#/ReaxFF##'`
svnurl="$svnurl/atomicdata/ForceFields/ReaxFF/Readme"
svnurltrunk=`echo $svnurl | sed -E 's#fixes/fix20[0-9]{2}#trunk#'`
echo "fetching $svnurl"
echo "fetching $svnurltrunk"
svn cat $svnurl > rxf_ffields_fix
svn cat $svnurltrunk > rxf_ffields_trunk
python parse_reaxff_ffields_list.py -i rxf_ffields_fix -o Included_Forcefields.rst
python parse_reaxff_ffields_list.py -i rxf_ffields_trunk -o Included_Forcefields_Trunk.rst --trunk
rm rxf_ffields_fix rxf_ffields_trunk

echo "DO NOT FORGET TO COMMIT THE .rst FILES !!! (after checking how they look like when building the doc)"

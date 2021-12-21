#!/bin/bash

# =========
# Defaults:
# =========

clean=true
build_pdf=false
nthreads=1
targets=( 'ADF' 'AMS' 'BAND' 'COSMO-RS' 'DFTB' 'ForceField' 'Hybrid' 'GFNFF' 'MOPAC' 'MLPotential' 'ReaxFF' 'OldReaxFF' 'Tutorials' 'GUI' 'Quild' 'Scripting' 'Installation' 'Ref_third_party' 'Documentation' 'plams' 'params' 'conformers' 'pyzacros' 'Metadocumentation')
build_full_doc=true

# For Mac OS X you might have to uncomment this:
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# ========================
# Defining some functions:
# ========================

CheckForBlockquotes () {
  # An annoying undocumented feature of Sphinx is that indented blocks with three or
  # more spaces are converted into html blockquotes. We don't want blockquotes in
  # our html, so when building I check that the resulting html has no blockquotes.
  echo "Checking for blockquotes... $1"
  if grep -ri -A3 -m 1 --include \*.html "<blockquote>" $1 ; then
     echo -e '\nWARNING - blockquote(s) found! See file(s) above.\n'
  fi
}

CheckForAboluteCrossLinks () {
  # Cross-links between documentation pages should be relative links,
  # and not absolute links to the website documentation.
  echo "Checking for absolute cross-links..."
  exclude_hit='https://www.scm.com/doc/Tutorials/GUI_overview/GUI_overview_tutorials.html'
  for f in $(find $1 -name '*.html') ; do
     if grep -v $exclude_hit $f | grep "www.scm.com/doc" ; then
        echo -e 'WARNING - Absolute link to from doc to www.scm.com/doc found in ' $f
        echo -e 'You should use relative links. \n'
     fi
  done
}

PrintHelp () {
   echo ""
   echo "Build the documentation."
   echo ""
   echo "Options:"
   echo "   -t   or --target:      Build only the specified target (e.g. -t ADF)"
   echo "   -k   or --keep:        Do not clean the build folder"
   echo "   -pdf or --build_pdf:   Build the pdf (requires latex)"
   echo "   -j:                    Number of threads to use when building the doc (serial by default)"
   echo ""
}

# =======================
# Beginning of the script
# =======================

export PATH=$AMSBIN:$PATH
SPHINX_BIN="$AMSBIN/amspython -m sphinx"

echo "Location of sphinx-build:" $SPHINX_BIN

# ================
# Parse the input:
# ================

while [[ $# > 0 ]]
do
   key="$1"
   case $key in
      -h|--help)
         PrintHelp
         exit 0
         ;;
      -t|--target)
         targets=( "$2" )
         build_full_doc=false
         shift
         ;;
      -k|--keep)
         clean=false
         ;;
      -pdf|--build_pdf)
         build_pdf=true
         ;;
      -j)
         nthreads=$2
         shift
         ;;
      *)
      echo "Unknown option:" $key
      exit 1
      ;;
   esac
   shift
done

# ==================
# Build the targets:
# ==================

export SCM_PYTHONPATH=$PWD:$SCM_PYTHONPATH # make the globalconf work with AMSHOME/bin/amspython
export PYTHONPATH=$PWD:$PYTHONPATH # make the globalconf work when not using AMSHOME/bin/amspython

for target in "${targets[@]}"
do

   source_location=$target
   build_location=build/$target

   # Plams is special: the .rst files are located in $AMSHOME/scripting/scm/plams/doc/source
   if [ "$target" = "plams" ] ; then
      source_location='../scripting/scm/plams/doc/source'
   fi

   # ParAMS is also special: the .rst files are located in $AMSHOME/scripting/scm/plams/doc/source
   if [ "$target" = "params" ] ; then
      source_location='../scripting/scm/params/doc/source'
   fi

   # Conformers is special too: the .rst files are located in $AMSHOME/scripting/scm/conformers/doc/source
   if [ "$target" = "conformers" ] ; then
      source_location='../scripting/scm/conformers/doc/source'
   fi

   # And pyzacros is special too: the .rst files are located in $AMSHOME/scripting/scm/pyzacros/doc/source
   if [ "$target" = "pyzacros" ] ; then
      source_location='../scripting/scm/pyzacros/doc/source'
   fi

   if $clean ; then
      echo "Cleaning the build dir..."
      rm -rf $build_location
   fi

   $SPHINX_BIN -j $nthreads -t scm_theme $source_location $build_location

   CheckForBlockquotes $build_location
   CheckForAboluteCrossLinks $build_location
done

# Fix the paths to the embedded videos in the documentation, see SCMSUITE-5959
echo "Fixing links to embedded videos..."
$AMSBIN/amspython misc/fix_video_links.py

# Check html hyperlinks between manuals
# (only if one is building the full doc, otherwise you will always get a ton of warnings)
if $build_full_doc ; then
  echo "Checking inter-document relative links..."
  $AMSBIN/amspython misc/check_links.py
fi

# copy mathjax into place
echo "Copying MathJax"
if test -d build/MathJax; then
  rm -rf build/MathJax
fi
cp -a MathJax build/MathJax

# ===========================
# (optionally) build the PDFs
# ===========================

if $build_pdf ; then
   for target in "${targets[@]}"
   do
     $SPHINX_BIN -b latex $target build/$target
     $SPHINX_BIN $target build/$target
     cd build/$target
     make
     cd ../..
   done
fi

#!/bin/bash
awk 'NF==4 {$1*=0.529177; $2*=0.529177; $3*=0.529177;} {print toupper($4), $1, $2, $3}' original_data.txt > angstrom_data.txt

awk '
BEGIN {counter=0; fn = "dummy.txt"}
/educt/ || /product/ {
    counter+= 1
    if ($0 ~/educt/) {
        fn = "e_" counter "_temp.xyz"
    }
    else {
        fn = "p_" counter-24 "_temp.xyz"
    }
}
{ print > fn }
' angstrom_data.txt

for f in *_temp.xyz
do
    renumberxyz.awk $f > ${f%_temp.xyz}.xyz
done

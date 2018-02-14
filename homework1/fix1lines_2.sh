#!/bin/bash
start=$(date +%s)
fnames=$(find . -name 'taqquote*.flr2')

echo $fnames

for line in $fnames ; do
   echo $line
   line2='edited'
   newFname=$line$line2;
   fdate=$(date -r $line +"%F")
   sed -r "s/\s+/,/; s/FLOW/\    /g; s/\    /,/; s/\s+//g; s/\ //g; s/$/,/; s/$/$fdate/" $line > $newFname
   head -n 10 $newFname ;
done
end=$(date +%s)
elapsed=$(( $end - $start ))
echo "$elapsed sec"

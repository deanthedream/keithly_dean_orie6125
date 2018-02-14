#!/bin/bash
start=$(date +%s)
fnames=$(find . -name 'taqquote*.flr2')

echo $fnames

for line in $fnames ; do
   echo $line
   line2='edited'
   newFname=$line$line2;
   sed -r 's/\s+/,/' $line > $newFname
   head -n 10 $newFname
   sed -r 's/FLOW/\    /g' $newFname > $newFname'2' ;
   head -n 10 $newFname'2' ;
   rm $newFname
   sudo sh -c 'echo 1 >/proc/sys/vm/drop_caches'
   sed -r 's/\    /,/' $newFname'2' > $newFname'3' ;
   head -n 10 $newFname'3'
   rm $newFname'2'
   sudo sh -c 'echo 1 >/proc/sys/vm/drop_caches'
   sed -r 's/\s+//g' $newFname'3' > $newFname'4' ;
   head -n 10 $newFname'4'
   rm $newFname'3'
   free
   sudo sh -c 'echo 1 >/proc/sys/vm/drop_caches'
   sed -r 's/\ //g' $newFname'4' > $newFname'5' ;
   head -n 10 $newFname'5'
   rm $newFname'4'
   sudo sh -c 'echo 1 >/proc/sys/vm/drop_caches'
   sed -r 's/$/,/' $newFname'5'  $newFname'6' ;
   head -n 10 $newFname'6'
   rm $newFname'5'
   free
   sudo sh -c 'echo 1 >/proc/sys/vm/drop_caches'
   free
   fdate=$(date -r $newFname'6' +"%F")
   sed -r "s/$/$fdate/" $newFname > $newFname'7' ;
   head -n 10 $newFname'7'
   rm $newFname'6'
   sudo sh -c 'echo 1 >/proc/sys/vm/drop_caches'
done
end=$(date +%s)
elapsed=$(( $end - $start ))
echo "$elapsed sec"

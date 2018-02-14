#!/bin/bash

fnames=$(find . -name 'taqquote*.flr')

echo $fnames

for line in $fnames ; do
   echo $line
   line2='edited'
   newFname=$line$line2;
   sed -r 's/\s+/,/' $line > $newFname
   #head -n 10 $newFname
   sed -r 's/FLOW/\    /g' $newFname > $newFname'2' ;
   #head -n 10 $newFname'2' ;
   sed -r 's/\    /,/' $newFname'2' > $newFname'3' ;
   #head -n 10 $newFname'3' ;
   sed -r 's/\s+//g' $newFname'3' > $newFname'4' ;
   sed -r 's/\ //g' $newFname'4' > $newFname'5' ;
   #head -n 10 $newFname'5' ;
   sed 's/$/,/' $newFname'5' > $newFname'6' ;
   #head -n 10 $newFname'6'
   fdate=$(date -r $newFname'6' +"%F")
   sed "s/$/$fdate/" $newFname'6' > $newFname'7' ;
   #head -n 10 $newFname'7'
   #echo $fdate
done

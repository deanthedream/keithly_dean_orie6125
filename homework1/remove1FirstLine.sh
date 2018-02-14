#!/bin/bash

fnames="taqquote20141201"   #$(find . -name 'taqquote*.full')

echo $fnames

for line in $fnames ; do
   echo $line
   line2=".flr2"
   newFname=$line$line2;
   #sed '1d' $line >> $newFname
   tail -n +2 $line >> $newFname
done

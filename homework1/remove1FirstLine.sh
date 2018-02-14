#!/bin/bash

fnames=$(find . -name 'taqquote*.full')

echo $fnames

for line in $fnames ; do
   echo $line
   line2=".flr"
   newFname=$line$line2;
   sed '1d' $line >> $newFname
done

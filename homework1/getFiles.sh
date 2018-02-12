#!/bin/bash
#this script gets the files necessary for homework1

#what files are in server
directory=taq.12.2014/
#locate_dir=$'s3://'$directory
#aws s3 ls locate_dir > fileNames.txt
filename='filenames.txt'
aws s3 ls s3://taq.12.2014/ > $filename

#filelines=`cat $filename` #this gets the lines in filename


head -n 7 $filename | sed -r 's/.*\s//' > filename2.txt #outputs first 7 lines of file to file
echo 'done reducing to 7 filenames'

filename2='filename2.txt'
filelines2=`cat $filename2`

for line in $filelines2 ; do #iterate through each line in filename
   echo $line
   locate_dir=$'s3://'$directory$line
   sudo aws s3 cp $locate_dir ./temp.zip;
   name_file="$(unzip -l temp.zip | awk '/-----/ {p = ++p % 2; next} p {print $NF}')";
   unzip temp.zip;
   rm -f temp.zip;
   head -n 1000 $name_file  > tmp_file;
   mv tmp_file $name_file
done
#physically grabs file from server
#sudo aws s3 cp s3://taq.12.2014/$filename




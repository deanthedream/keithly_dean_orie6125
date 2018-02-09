#!/bin/bash
#this script gets the files necessary for homework1

#what files are in server
#directory=taq.12.2014/
#locate_dir=$'s3://'$directory
#aws s3 ls locate_dir > fileNames.txt
aws s3 ls s3://taq.12.2014/ > filenames.txt
#s3cmd ls -r locate_dir | awk '{print $4}' > objects_in_bucket


#physically grabs file from server
#sudo aws s3 cp s3://taq.12.2014/$filename

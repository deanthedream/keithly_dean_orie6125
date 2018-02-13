Written by Dean Keithly

Running the getFiles.sh script will create a file containing all the filenames in the s3 bucket
these files are then reduced to only the first 7 filenames in filenames2
these 7 files are then retrieved from the repository and the first 1000 lines are saved to disc as taqquote*

Running removeFirstLines.sh removes the first lines of all taqquote* files creating taqquote*.flr



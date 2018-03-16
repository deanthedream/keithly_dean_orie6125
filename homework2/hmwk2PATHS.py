import sys
import os
import re
import fnmatch
#fnmatch.filter(os.listdir('.'), )
files = [f for f in os.listdir('.') if os.path.isdir(f)] # Get dir in current dir
files2 = [f for f in files if not '.' in f] # remove filename if there is a dot in it
files3 = list()
folderExclusion = ['tests','env','coverage','htmlcov']
for folderName in files2:
    if not folderName in folderExclusion:
        files3.append(folderName)
        sys.path.append(os.path.join(os.getcwd()+'/'+folderName))
sys.path.append(os.path.join(os.getcwd()))


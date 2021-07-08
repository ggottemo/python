#! python3 
#copyToSeperate.py - From Automate the Boring Stuff
import shutil, os, re
from pathlib import Path

def copyToSeperate(folder, dest):
    folder = os.path.abspath(folder) #make sure the folder is absolute
    dest = os.path.abspath(dest)
    suffix = '.py' #suffix variable to allow for change later
    number = 0 # Number of files copied
    fileRegex = re.compile(rf'''
                 (^.*?)  #accept any text at the begining
                 
                 ({suffix}$) #suffix at the end
                 
                 
                 
                 
                 
                 ''', re.VERBOSE )   
    print(f'Copying files to {dest}')
    #walkthrough tree searching for certain file type
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if fileRegex.match(filename) != None and foldername == folder:
                shutil.copy(filename, dest)    
                print(f'Copying file {filename}')
                number += 1 

    print(f'{number} of items have been copied')
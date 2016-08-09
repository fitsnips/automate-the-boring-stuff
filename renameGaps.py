#! python3
# reanameGaps.py - find gaps in a file order and fix by downshifting

import os, shutil

def renameGaps(folder):
    folder = os.path.abspath(folder)

    myindex = 1  # we need to start at one as we do not want 000.txt file

    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder,file)) and 'spam' in file:
            currentFile = 'spam00' + str(myindex) + '.txt'
            fcurrentFile = os.path.join(folder,currentFile)
            ffile = os.path.join(folder,file)
            if file != currentFile:
                shutil.move(ffile,fcurrentFile)
            myindex += 1





renameGaps('/tmp/python-test')
#! python3
# findeLarge.py - Find large files or directories in a given path

import os, shutil

def findLarge(folder):

    folder = os.path.abspath(folder)

    for folder, subfolders, filenames in os.walk(folder):

        # for subfolder in subfolders:
        #     tfolder = os.path.join(folder,subfolder)
        #     fsize = os.path.getsize(tfolder)
        #     print(str(fsize))

        for filename in filenames:
            tfile = os.path.join(folder,filename)
            size = os.path.getsize(tfile)

            #print('Size is equal to ' + str(size) )
            if size >= 102400000: # 100Mb
                print('%s size greater then 100M ' % filename)


findLarge('/tmp/python-test')




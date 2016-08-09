#! python3

import os, shutil

def copyToFolder(sfolder,dfolder):
    sfolder = os.path.abspath(sfolder)
    dfolder = os.path.abspath(dfolder)

    # Walk the entire folder
    for foldername, subfolders, filenames in os.walk(sfolder):
        print('Foldername: ' + foldername )
        if foldername != dfolder:
            for filename in filenames:
                if filename.endswith('.pdf'):
                    sfile = os.path.join(foldername,filename)
                    dfile = os.path.join(dfolder,filename)
                    print(sfile)
                    shutil.copy2(sfile,dfile)

    print('Done')

copyToFolder('/Users/jmiller/PycharmProjects/automate-the-boring-stuff/','/Users/jmiller/PycharmProjects/automate-the-boring-stuff/pdfs/')
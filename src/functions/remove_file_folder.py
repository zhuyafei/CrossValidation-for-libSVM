# -*- coding: utf-8 -*-  
#coding=utf-8 
'''
Created on 2014年8月14日

@author: songying
'''

import os
import shutil
def remove_file_folder(rootdir):
    filelist=[]
#     rootdir="../../data/cross_validation"
    filelist=os.listdir(rootdir)
    for f in filelist:
        filepath = os.path.join( rootdir, f )
        if os.path.isfile(filepath):
            os.remove(filepath)
            #print filepath+" removed!"
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath,True)
            #print "dir "+filepath+" removed!"
    return 0

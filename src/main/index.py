# -*- coding: utf-8 -*-  
#coding=utf-8 
'''
Created on 2014年8月14日

@author: songying
'''
import os
from include.header import log_name
from include.header import rootdir_cross_validation
from include.header import rootdir_output
from functions.remove_file_folder import remove_file_folder
#init
remove_file_folder(rootdir_cross_validation)
remove_file_folder(rootdir_output)
print "initialization done!"
file_log = open(log_name, 'w')

command1 = "python 01get_n_subset.py"
run1 = os.popen(command1)
print run1.read().strip('\n')

command2 = "python 02prediction.py"
run2 = os.popen(command2)
print run2.read().strip('\n')

command3 = "python 03averageResult.py"
run3 = os.popen(command3)
print run3.read().strip('\n')

print "index Done!!!"
file_log.close()
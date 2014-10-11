# -*- coding: utf-8 -*-  
#coding=utf-8 
'''
Created on 2014年8月5日

@author: songying
'''
import os
from include.header import n_fold
from include.header import path_cross_prefix
from include.header import log_name
from include.header import train_command
from include.header import test_command
out_log = open(log_name, 'a')
out_log.write("\n################开始对每次交叉验证进行预测################\n")
for iter in range(1, n_fold+1):
    train_command_new = "..\..\libsvm\windows\\" + train_command + " ..\..\data\cross_validation\\fold_" + str(iter) + "\\train.txt" + " ..\..\data\cross_validation\\fold_" + str(iter) + "\model.txt"
    train = os.popen(train_command_new)
    out_log = open(log_name, 'a')
    out_log.write("\n##################第"+str(iter)+"次验证#################\n")
    out_log.write(train.read())
    
    test_command_new = "..\..\libsvm\windows\\" + test_command + " ..\..\data\cross_validation\\fold_" + str(iter) + "\\test.txt" + " ..\..\data\cross_validation\\fold_" + str(iter) + "\model.txt" + " ..\..\data\cross_validation\\fold_" + str(iter) + "\\result.txt"
    test = os.popen(test_command_new)
    out_log.write(test.read())
    out_log.write("cross"+str(iter)+" Done!!!\n\n")

    out_log.close()
    
print "02------>prediction Done!"




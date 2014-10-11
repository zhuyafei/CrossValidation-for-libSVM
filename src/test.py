# -*- coding: utf-8 -*-  
#coding=utf-8 
'''
Created on 2014年8月14日

@author: songying
'''
import sys
print "scrip name\t", sys.argv[0]
for i in range(1, len(sys.argv)):
    print "parameter\t" + str(i) +'\t'+ str(sys.argv[i])

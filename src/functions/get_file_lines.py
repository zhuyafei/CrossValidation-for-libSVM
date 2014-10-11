# -*- coding: utf-8 -*-  
#coding=utf-8 
'''
Created on 2014年8月4日

@author: songying
'''
import os
import sys

def get_file_lines(file_name):
    line_count = 0
    line = file_name.readline()
    while line != '':
        line_count += 1
        line = file_name.readline()
    file_name.close()
    return line_count
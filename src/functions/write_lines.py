# -*- coding: utf-8 -*-  
#coding=utf-8 
'''
Created on 2014年8月4日

@author: songying
'''
import os
import sys
from include.header import file_negative_name
from include.header import file_positive_name

def write_lines_train(out_file_name, positive_array, negative_array):
    file_positive = open(file_positive_name, 'r')
    file_negative = open(file_negative_name, 'r')
    outfile = open(out_file_name, 'w')
    if positive_array[1] == 0:
        for i_positive in range((positive_array[2] - 1)):
            file_positive.readline()
        for j_positive in range(positive_array[3]):
            outfile.write(file_positive.readline())

        for i_negative in range((negative_array[2] - 1)):
            file_negative.readline()
        for j_negative in range(negative_array[3]):
            outfile.write(file_negative.readline())
            
    if positive_array[1] != 0:
        for i_positive in range(positive_array[1]):
            outfile.write(file_positive.readline())
        for j_positive in range((positive_array[2]-positive_array[1]-1)):
            file_positive.readline()
        for k_positive in range(positive_array[3]):
            outfile.write(file_positive.readline())
            
        for i_negative in range(negative_array[1]):
            outfile.write(file_negative.readline())
        for j_negative in range(negative_array[2]-negative_array[1]-1):
            file_positive.readline()
        for k_negative in range(negative_array[3]):
            outfile.write(file_negative.readline())
    file_positive.close()
    file_negative.close()
    outfile.close()
    return 0

def write_lines_test(out_file_name, positive_array, negative_array):
    file_positive = open(file_positive_name, 'r')
    file_negative = open(file_negative_name, 'r')
    outfile = open(out_file_name, 'w')
    if positive_array[0] == 0:
        for i in range(positive_array[1]):
            outfile.write(file_positive.readline())
        for j in range(negative_array[1]):
            outfile.write(file_negative.readline())
    if positive_array[0] != 0:
        for i in range(positive_array[0]):
            file_positive.readline()
        for j in range(positive_array[1]):
            outfile.write(file_positive.readline())
            
        for i in range(negative_array[0]):
            file_negative.readline()
        for j in range(negative_array[1]):
            outfile.write(file_negative.readline())
    file_positive.close()
    file_negative.close()
    outfile.close()
    return 0


def write_lines_last(train_file_name, test_file_name, positive_train, positive_test, negative_train, negative_test):
    file_positive = open(file_positive_name, 'r')
    file_negative = open(file_negative_name, 'r')
    outfile_train = open(train_file_name, 'w')
    outfile_test = open(test_file_name, 'w')
    for i in range(positive_train):
        outfile_train.write(file_positive.readline())
    for i in range(negative_train):
        outfile_train.write(file_negative.readline())
    for j in range(positive_test):
        outfile_test.write(file_positive.readline())
    for j in range(negative_test):
        outfile_test.write(file_negative.readline())
    
    file_positive.close()
    file_negative.close()
    outfile_train.close()
    outfile_test.close()
    return 0




# -*- coding: utf-8 -*-  
#coding=utf-8 
'''
Created on 2014年8月5日

@author: songying
'''
from math import sqrt
def getTP_TN_FP_FN(file_name, positive_num):
    array = [0] * 4
    line = file_name.readline()
    line = file_name.readline()
    count = 1
    while line != '':
        line1 = ''.join(line).split(' ')
        if count < positive_num + 1:
            if line1[0] == '1':
                array[0] += 1
            else:
                array[3] += 1
        if count > positive_num:
            if line1[0] == '-1':
                array[1] += 1
            else:
                array[2] += 1
        
        line = file_name.readline()
        count += 1
    return array

def getRecall(TP, TN, FP, FN):
    recall = float(TP) / float(TP + FN)
    return recall
def getPrecision(TP, TN, FP, FN):
    precision = float(TP) / float(TP + FP)
    return precision
def getACC(TP, TN, FP, FN):
    acc = float(TP + TN) / float(TP + FP + FN + TN)
    return acc
def getSP(TP, TN, FP, FN):
    sp = float(TN) / float(TN + FP)
    return sp
def getF_measure(TP, TN, FP, FN):
    f_measure = 2 * float(TP) / float(2 * TP + FP + FN)
    return f_measure
def getMCC(TP, TN, FP, FN):
    mcc = float(TP * TN - FP * FN) / sqrt(float((TP + FN) * (TP + FP) * (TN + FP) * (TN + FN)))
    return mcc



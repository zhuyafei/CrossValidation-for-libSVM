# -*- coding: utf-8 -*-  
#coding=utf-8 
'''
Created on 2014年8月5日

@author: songying
'''
from include.header import *
from functions.get_file_lines import get_file_lines
from functions.mertric import *

##########求得正负样本的行数############
file_negative = open(file_negative_name, 'r')
file_positive = open(file_positive_name, 'r')
#

positive_line_count = get_file_lines(file_positive)
negative_line_count = get_file_lines(file_negative)

each_negative_subset_count = negative_line_count / n_fold
last_negative_subset_count = negative_line_count - each_negative_subset_count * (n_fold - 1)
each_positive_subset_count = positive_line_count / n_fold
last_positive_subset_count = positive_line_count - each_positive_subset_count * (n_fold - 1)

negative_array = [0]*n_fold
positive_array = [0]*n_fold

recall = [0.0]*n_fold
precision = [0.0]*n_fold
ACC = [0.0]*n_fold
SP = [0.0]*n_fold
F_measure = [0.0]*n_fold
MCC = [0.0]*n_fold
#记录每次交叉实验中样例的个数
for i in range(n_fold-1):
    positive_array[i] = each_positive_subset_count
positive_array[n_fold-1] = last_positive_subset_count

#求出每次交叉验证的指标
for iter in range(1, n_fold + 1):
    file_name = path_cross_prefix + str(iter) + "/result.txt"
    file_result = open(file_name, 'r')
    TP_TN_FP_FN = getTP_TN_FP_FN(file_result, positive_array[iter - 1])
    TP = TP_TN_FP_FN[0]
    TN = TP_TN_FP_FN[1]
    FP = TP_TN_FP_FN[2]
    FN = TP_TN_FP_FN[3]
#     print TP_TN_FP_FN
    recall[iter - 1] = getRecall(TP, TN, FP, FN)
    precision[iter - 1] = getPrecision(TP, TN, FP, FN)
    ACC[iter - 1] = getACC(TP, TN, FP, FN)
    SP[iter - 1] = getSP(TP, TN, FP, FN)
    F_measure[iter - 1] = getF_measure(TP, TN, FP, FN)
    MCC[iter - 1] = getMCC(TP, TN, FP, FN)

#求出交叉验证的平均指标
totalRecall = 0.0
totalPrecision = 0.0
totalACC = 0.0
totalSP = 0.0
totalF_measure = 0.0
totalMCC = 0.0
for i in range(n_fold):
    totalRecall += recall[i]
    totalPrecision += precision[i]
    totalACC += ACC[i]
    totalSP += SP[i]
    totalF_measure += F_measure[i]
    totalMCC += MCC[i]
averageRecall = totalRecall / n_fold
averagePrecision = totalPrecision / n_fold
averageACC = totalACC / n_fold
averageSP = totalSP / n_fold
averageF_measure = totalF_measure / n_fold
averageMCC = totalMCC / n_fold

outfile = open(outfile_name, 'w')
outfile.write(str(n_fold) + " average cross validation result:\n")
outfile.write("Average Recall:\t" + str(averageRecall) + '\n')
outfile.write("Average Precision:\t" + str(averagePrecision) + '\n')
outfile.write("Average ACC:\t" + str(averageACC) + '\n')
outfile.write("Average SP:\t" + str(averageSP) + '\n')
outfile.write("Average F_measure:\t" + str(averageF_measure) + '\n')
outfile.write("Average MCC:\t" + str(averageMCC) + '\n')

file_log = open(log_name, 'a')
file_log.write("##################每次交叉验证的各个指标明细##################\n")
file_log.write("Recall:\t" + str(recall) + '\n')
file_log.write("Precision:\t" + str(precision) + '\n')
file_log.write("ACC:\t" + str(ACC) + '\n')
file_log.write("SP:\t" + str(SP) + '\n')
file_log.write("F_measure:\t" + str(F_measure) + '\n')
file_log.write("MCC:\t" + str(MCC) + '\n\n')

file_log.write("##################交叉验证的平均最后结果##################\n")
file_log.write("Average Recall:\t" + str(averageRecall) + '\n')
file_log.write("Average Precision:\t" + str(averagePrecision) + '\n')
file_log.write("Average ACC:\t" + str(averageACC) + '\n')
file_log.write("Average SP:\t" + str(averageSP) + '\n')
file_log.write("Average F_measure:\t" + str(averageF_measure) + '\n')
file_log.write("Average MCC:\t" + str(averageMCC) + '\n')

print "03------>averageResult Done!"
print "......................................................"
print str(n_fold) + " average cross validation result:\n"
print "Average Recall:\t" + str(averageRecall)
print "Average Precision:\t" + str(averagePrecision)
print "Average ACC:\t" + str(averageACC)
print "Average SP:\t" + str(averageSP)
print "Average F_measure:\t" + str(averageF_measure)
print "Average MCC:\t" + str(averageMCC)
print "......................................................"
outfile.close()
file_log.close()
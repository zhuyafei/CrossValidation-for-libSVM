# -*- coding: utf-8 -*-  
#coding=utf-8 
'''
Created on 2014年8月4日

@author: songying
'''
import os
from include.header import *
from functions.get_file_lines import get_file_lines
from functions.write_lines import write_lines_train
from functions.write_lines import write_lines_test
from functions.write_lines import write_lines_last

import datetime

##########求得正负样本的行数############
file_negative = open(file_negative_name, 'r')
file_positive = open(file_positive_name, 'r')
file_log = open(log_name, 'a')

now = datetime.datetime.now()
file_log.write("当前执行时间： "+ str(now)[0:-7] + '\n')

positive_line_count = get_file_lines(file_positive)
negative_line_count = get_file_lines(file_negative)
file_log.write("负样本总共：\t"+str(negative_line_count) + '\n')
file_log.write("正样本总共：\t"+str(positive_line_count) + '\n')

##############把输入的正负样本，拆分为n_fold个子集#############
each_negative_subset_count = negative_line_count / n_fold
last_negative_subset_count = negative_line_count - each_negative_subset_count * (n_fold - 1)
each_positive_subset_count = positive_line_count / n_fold
last_positive_subset_count = positive_line_count - each_positive_subset_count * (n_fold - 1)
# print each_negative_subset_count
# print last_negative_subset_count
for iter in range(1, n_fold+1):
    if iter < n_fold:
        test_set_negative = [(iter-1)*each_negative_subset_count, each_negative_subset_count]
        train_set_negative = [1, (iter-1)*each_negative_subset_count, iter*each_negative_subset_count+1, negative_line_count - iter*each_negative_subset_count]
        test_set_positive = [(iter-1)*each_positive_subset_count, each_positive_subset_count]
        train_set_positive = [1, (iter-1)*each_positive_subset_count, iter*each_positive_subset_count+1, positive_line_count - iter*each_positive_subset_count]
        #make folder
        path = "../../data/cross_validation"
        folder_name = "fold_"+str(iter)
        new_path = os.path.join(path, folder_name)
        if not os.path.isdir(new_path):
            os.makedirs(new_path)
        file_train_name = path_cross_prefix + str(iter) + "/train.txt"
        file_test_name = path_cross_prefix + str(iter) + "/test.txt"
        write_lines_train(file_train_name, train_set_positive, train_set_negative)
        write_lines_test(file_test_name, test_set_positive, test_set_negative)
    #the last cross validation
    if iter == n_fold:
        path = "../../data/cross_validation"
        folder_name = "fold_"+str(iter)
        new_path = os.path.join(path, folder_name)
        if not os.path.isdir(new_path):
            os.makedirs(new_path)
        file_train_name = path_cross_prefix + str(n_fold) + "/train.txt"
        file_test_name = path_cross_prefix + str(n_fold) + "/test.txt"
        write_lines_last(file_train_name, file_test_name, (n_fold-1)*each_positive_subset_count, last_positive_subset_count, (n_fold-1)*each_negative_subset_count, last_negative_subset_count)

file_log.write(str(n_fold) + "子集拆分完毕！")
print "01------>get_n_subset Done!"



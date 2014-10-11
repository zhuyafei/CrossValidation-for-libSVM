# -*- coding: utf-8 -*-  
#coding=utf-8 
'''
Created on 2014年8月4日

@author: songying
'''
#n倍交叉,如果需要其他交叉倍数，作适当修改
n_fold = 10
#train和predict的命令，这里是我定义的一种命令
#-s:0,-t:0,-c:100,-b:1,-h:0,-v:10
train_command = "svm-train.exe -s 0 -t 0 -c 100 -b 1 -h 0"
test_command = "svm-predict.exe -b 1"

#输入的正负样本路径
file_negative_name = "../../data/original_data/negative.txt"
file_positive_name = "../../data/original_data/positive.txt"
#输出日志路径
log_name = "../../data/output/logs.txt"
#交叉验证输出的路径前缀
path_cross_prefix = "../../data/cross_validation/fold_"
#输出结果文件路径
outfile_name = "../../data/output/out.txt"
#产生数据的文件夹路径
rootdir_cross_validation="../../data/cross_validation"
rootdir_output="../../data/output"
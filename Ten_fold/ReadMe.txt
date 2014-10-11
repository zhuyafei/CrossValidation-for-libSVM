##########版本介绍##########
程序包版本：0.1
程序包作者：songying
程序包网址：www.chengzhanzhan.cn

##########目的##########
使用过libsvm的用户会注意到，当做n倍交叉验证时，libsvm只给出了一个ACC，而对于MCC，F-measure等指标，则没有给出。而本程序包的功能在于，只要输入对应的正负样本文件，以及输入对应的参数，就会给出Recall, Precision, ACC, Specificity(SP), Accuracy, F-measure, Matthew's correlation coefficient（MCC）等结果。各个指标的计算公式如下：
	Recall = TP / (TP + FN)
	Precision = TP / (TP + FP)
	ACC = (TP + TN) / (TP + FP + FN + TN)
	SP = TN / (TN + FP)
	F-measure = 2 * TP / (2 * TP + FP + FN)
	MCC = (TP * TN - FP * FN) / sqrt((TP + FN) * (TP + FP) * (TN + FP) * (TN + FN))
其中，TP，FP，TN及FN代表true positive, false positive, true negative及false negative。

##########程序包功能############
支持自定义交叉验证的命令参数
能够支持2-99倍交叉验证
给出了每次交叉验证的训练集，测试集以及训练所得到的模型及最终的预测结果。
给出了每次交叉验证的以上各项指标的结果
给出了最终n次交叉验证的平均结果

############输入文件要求#########
输入文件包含正负样本，，文件名要求为：positive.txt（表示正样本）和negative.txt（表示负样本）。
对于用户自定义的输入文件，放置在data/original_data文件夹下（以包含了两个demo文件），替换原来的文件即可。
每行数据格式同libsvm的格式完全相同，例如：
	1 1:0.0066 2:0.0171 4:0.0066 6:0.0247 7:0.0228
	-1 1:0.0067 2:0.0150 4:0.0114 6:0.0150 7:0.0150 11:0.0225

############输出结果###############
程序给出了指标的平均运算结果：
	initialization done!
	01------>get_10_subset Done!
	02------>prediction Done!
	03------>averageResult Done!
	......................................................
	10 average cross validation result:

	Average Recall:	1.0
	Average Precision:	1.0
	Average ACC:	1.0
	Average SP:	1.0
	Average F_measure:	1.0
	Average MCC:	1.0
	......................................................
	index Done!!!
在data/output文件夹下，也可以找到out.txt文件，该文件即为输出结果。
对于运算过程，本程序也给出了详细的log，可供用户进行查看，对应的文件为logs.txt。

##########程序演示################
1、打开src/include/header.py文件，修改参数：
	修改交叉验证次数：这里n_fold = 10
	修改train命令，这里定义的为：svm-train.exe -s 0 -t 0 -c 100 -b 1 -h 0
2、执行src/main/index.py即可

##########未来展望################
本程序包功能会继续进行完善。
# -*- coding: utf-8 -*- 
# @Time : 2019/11/18 16:36 
# @Author : 赵金林
# @Site :  
# @File : 素数.py


l = []
for x in range(100):
    #判断如果ｘ是素数，则打印，如果不是素数就跳过
    if x <2:
        continue
    for i in range(2,x):
        if x % i == 0:
            break
    else:
        l.append(x)

print(l)


#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/14 22:52 
# @Author : 赵金林
# @Site :  
# @File : Quick_Sort.py 
# @Software: PyCharm

# 方法1
def select_sort(sum):
    for i in range(0, len(sum) - 1):
        index = i
        for j in range(i + 1, len(sum)):
            if sum[index] > sum[j]:
                index = j
        sum[i], sum[index] = sum[index], sum[i]
    return sum


print(select_sort([84, 89, 61, 88, 87]))
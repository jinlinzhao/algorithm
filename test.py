# -*- coding: utf-8 -*- 
# @Time : 2019/11/8 10:46 
# @Author : 赵金林
# @Site :  
# @File : test.py

def neighbors(node):
    for i in range(4):
        x = int(node[i])
        for d in (-1, 1):
            y = (x + d) % 10
            yield node[:i] + str(y) + node[i + 1:]


node = '0000'
for i in range(4):
    x = int(node[i])
    for j in (-1, 1):
        y = (x + j) % 10
        print(node[:i]+str(y)+node[i+1:])

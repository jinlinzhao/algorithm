# -*- coding: utf-8 -*- 
# @Time : 2019/11/18 15:45 
# @Author : 赵金林
# @Site :  
# @File : test.py

import sys

# line = sys.stdin.readline().strip()
# print(line)  # 输出的字符串
#
# n = int(input())
# print(n)  # 输出为数字
#
# l = list(map(int, input().split(" ")))
# print(l)  # 单行输入输出为数组

if __name__ == "__main__":
    data = []
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    tmp = list(map(int, line.split(" ")))
    data.append(tmp)
print(data)  # 输出形式为矩阵

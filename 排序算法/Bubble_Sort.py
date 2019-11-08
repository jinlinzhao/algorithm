# -*- coding: utf-8 -*- 
# @Time : 2019/11/7 14:00 
# @Author : 赵金林
# @Site : 冒泡算法
# @File : Bubble_Sort.py


def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li) - 1-i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
        print(li)


li = [2, 5, 7, 1, 9, 3, 0]
print(li)
bubble_sort(li)
print(li)

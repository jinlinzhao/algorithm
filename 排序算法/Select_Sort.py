# -*- coding: utf-8 -*- 
# @Time : 2019/11/7 14:11 
# @Author : 赵金林
# @Site :  选择排序
# @File : Select_Sort.py

def select_sort(li):
    for i in range(0, len(li) - 1):
        tmp = i
        for j in range(i+1, len(li)):
            if li[j] < li[tmp]:
                tmp = j
        li[i], li[tmp] = li[tmp], li[i]
        print(li)

li = [2, 5, 7, 1, 9, 3, 0]
print(li)
select_sort(li)
print(li)

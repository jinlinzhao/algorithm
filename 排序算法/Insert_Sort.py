# -*- coding: utf-8 -*- 
# @Time : 2019/11/7 14:17 
# @Author : 赵金林
# @Site :  插入排序,这个还是有一点的绕啊
# @File : Insert_Sort.py
def insert_sort(li):
    for i in range(1, len(li)):
        preIndex = i - 1  # 手里面的牌的索引
        current = li[i]  # 拿到的牌
        # 在手里面的牌中遍历，看需要插入到那个地方
        while preIndex >= 0 and li[preIndex] > current:  # 看看拿到的牌需要放在什么地方
            li[preIndex + 1] = li[preIndex]
            preIndex -= 1
        li[preIndex + 1] = current
        print(li)


li = [7, 4, 5, 1, 9, 3, 0]
print(li)
insert_sort(li)

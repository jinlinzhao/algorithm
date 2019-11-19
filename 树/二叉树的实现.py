# -*- coding: utf-8 -*- 
# @Time : 2019/11/18 16:00 
# @Author : 赵金林
# @Site :  
# @File : 二叉树的实现.py
from collections import deque


class BTree:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左子树
        self.rchild = None  # 右子树


def level_order(root):
    '''
    层次遍历，使用python的内置队列实现
    :param root:
    :return:
    '''
    if root:
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
            node = queue.popleft()
            print(node.data)
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)


def copy_tree(root):
    '''
    二叉树镜像，左右二叉树交换位置
    :param root:
    :return:
    '''
    if root:
        # temp = root.lchild
        # root.lchild = root.rchild
        # root.rchild = temp
        root.lchild, root.rchild = root.rchild, root.lchild
        copy_tree(root.lchild)
        copy_tree(root.rchild)


a = BTree("A")
b = BTree("B")
c = BTree("C")
d = BTree("D")
e = BTree("E")
f = BTree("F")
g = BTree("G")
a.lchild = b
a.rchild = c
b.lchild = d
b.rchild = e
c.lchild = f
c.rchild = g
root = a
level_order(root)
copy_tree(root)
print("*" * 20)
level_order(root)

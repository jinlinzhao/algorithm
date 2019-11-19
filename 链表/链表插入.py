# -*- coding: utf-8 -*- 
# @Time : 2019/11/15 16:34 
# @Author : 赵金林
# @Site :  
# @File : 链表插入.py

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedLIst():
    def __init__(self):
        self.length = 0
        self.head = None

    def append(self, node):
        if isinstance(node, ListNode):
            pass
        else:
            node = ListNode(node)
        if self.is_empty():
            self.head = node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = node
        self.length += 1

    def is_empty(self):
        return self.length == 0

    def printList(self):
        if self.length == 0:
            return None
        else:
            p = self.head
            while p.next:
                print(p.val, '--->', end='')
                p = p.next
            print(p.val)

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
s = LinkedLIst()
s.append(a)
s.append(b)
s.append(c)
s.append(d)
s.append(e)
s.printList()
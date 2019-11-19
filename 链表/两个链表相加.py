# -*- coding: utf-8 -*- 
# @Time : 2019/11/18 16:48 
# @Author : 赵金林
# @Site :  
# @File : 两个链表相加.py

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head):
    p = None
    q = None
    p = head.next
    while p.next !=None:
        q = p.next
        p.next = q.next
        q.next = p
        head.next = q
    p.next = head
    head = p.next.next
    p.next.next = None
    return head


def printList(head):
    if head:
        p = head
        while p.next:
            print(p.val, '--->', end='')
            p = p.next
        print(p.val)


a = ListNode(9)
a.next = ListNode(3)
a.next.next = ListNode(7)
c = reverse_list(a)
printList(c)
b = ListNode(6)
b.next = ListNode(3)
printList(b)

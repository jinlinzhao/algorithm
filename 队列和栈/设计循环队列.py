# -*- coding: utf-8 -*- 
# @Time : 2019/11/8 11:42 
# @Author : 赵金林
# @Site :  
# @File : 设计循环队列.py
'''
设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：
MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。
'''


class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [0 for _ in range(k + 1)]
        self.size = k + 1
        self.front = 0
        self.rear = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        向循环队列插入一个元素。如果成功插入则返回真。
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            return True
        return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        从循环队列中删除一个元素。如果成功删除则返回真。
        :rtype: bool
        """
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            return True
        return False

    def Front(self):
        """
        Get the front item from the queue.
        从队首获取元素。如果队列为空，返回 -1
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[(self.front + 1) % self.size]
        return -1

    def Rear(self):
        """
        Get the last item from the queue.
        获取队尾元素。如果队列为空，返回 -1
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[(self.rear) % self.size]
        return -1

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        检查循环队列是否为空
        :rtype: bool
        """
        return self.rear == self.front

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        检查循环队列是否已满
        :rtype: bool
        """
        return (self.rear + 1) % self.size == self.front


# Your MyCircularQueue object will be instantiated and called as such:
circularQueue = MyCircularQueue(3)  # 设置长度为 3

print(circularQueue.enQueue(1))  # 返回 true

print(circularQueue.enQueue(2))  # 返回 true

print(circularQueue.enQueue(3))  # 返回 true

print(circularQueue.enQueue(4))  # 返回 false，队列已满

print(circularQueue.Rear())  # 返回 3

print(circularQueue.isFull())  # 返回 true

print(circularQueue.deQueue())  # 返回 true

print(circularQueue.enQueue(4))  # 返回 true

print(circularQueue.Rear())  # 返回 4

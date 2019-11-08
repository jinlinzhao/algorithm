# -*- coding: utf-8 -*- 
# @Time : 2019/11/8 15:40 
# @Author : 赵金林
# @Site :  
# @File : 打开转盘锁.py
import collections


class Solution(object):
    def openLock(self, deadends, target):
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i + 1:]

        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node in dead: continue
            if node == target: return depth
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1))
        return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0101"
a = Solution()
print(a.openLock(deadends, target))

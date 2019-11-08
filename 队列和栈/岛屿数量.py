# -*- coding: utf-8 -*- 
# @Time : 2019/11/8 15:34 
# @Author : 赵金林
# @Site :  队列和广度优先搜索
# @File : 岛屿数量.py
'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3
'''

from collections import deque


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        dirs = [
            lambda x, y: (x + 1, y),
            lambda x, y: (x - 1, y),
            lambda x, y: (x, y + 1),
            lambda x, y: (x, y - 1)
        ]

        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    queue = deque()
                    num += 1
                    queue.append((i, j))
                    while len(queue) > 0:
                        cur_node = queue.popleft()
                        for dir in dirs:
                            next_code = dir(cur_node[0], cur_node[1])
                            if next_code[0] > len(grid) - 1 or next_code[1] > len(grid[0]) - 1 or next_code[0] == -1 or \
                                    next_code[1] == -1:
                                continue
                            if grid[next_code[0]][next_code[1]] == "1":
                                queue.append((next_code[0], next_code[1]))
                                grid[next_code[0]][next_code[1]] = "2"
        return num

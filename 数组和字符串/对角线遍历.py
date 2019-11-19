# -*- coding: utf-8 -*- 
# @Time : 2019/11/11 11:10 
# @Author : 赵金林
# @Site :  
# @File : 对角线遍历.py
'''

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出:  [1,2,4,7,5,3,6,8,9]
'''


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return [0]
        iNum = len(matrix)
        jNum = len(matrix[0])
        result = []
        isUp = True
        resultIndex = 0
        iIndex = 0
        jIndex = 0
        while iIndex < iNum and jIndex < jNum:
            if isUp:
                while iIndex >= 0 and jIndex >= 0 and iIndex < iNum and jIndex < jNum:
                    result[resultIndex] = matrix[iIndex][jIndex]

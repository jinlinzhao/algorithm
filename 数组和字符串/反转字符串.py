# -*- coding: utf-8 -*- 
# @Time : 2019/11/4 16:30 
# @Author : 赵金林
# @Site :  
# @File : 反转字符串.py

'''
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
'''

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        left_point = 0
        right_point = len(s) - 1
        for _ in s:
            if left_point == right_point or left_point>right_point:
                return s
            s[left_point], s[right_point] = s[right_point], s[left_point]
            left_point += 1
            right_point -= 1


if __name__ == '__main__':
    s = ["H", "a", "n", "n", "a", "h"]
    a = Solution()
    print(a.reverseString(s))

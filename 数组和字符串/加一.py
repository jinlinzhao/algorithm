# -*- coding: utf-8 -*- 
# @Time : 2019/11/4 13:33 
# @Author : 赵金林
# @Site :  
# @File : 加一.py
'''
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
'''
class Solution:
    def plusOne(self, digits):
        num = 0
        for i in range(0, len(digits)):
            num += digits[i] * (10 ** (len(digits) - i-1))
        num +=1
        print(num)
        return [int(j) for j in str(num)]

if __name__ == '__main__':
    nums = [1, 9, 9]
    a = Solution()
    print(a.plusOne(nums))

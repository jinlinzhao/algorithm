# -*- coding: utf-8 -*- 
# @Time : 2019/11/4 9:57 
# @Author : 赵金林
# @Site :  
# @File : 寻找数组的中心索引.py
'''
输入:
nums = [1, 7, 3, 6, 5, 6]
输出: 3
解释:
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。
'''
class Solution:
    def pivotIndex(self, nums):
        right_sum = sum(nums)
        left_sum = 0
        for i in range(0,len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1

if __name__ == '__main__':
    nums = [1, 2, 3]
    a = Solution()
    print(a.pivotIndex(nums))

# -*- coding: utf-8 -*- 
# @Time : 2019/11/4 16:57 
# @Author : 赵金林
# @Site :  
# @File : 数组拆分 I.py
'''
输入: [1,4,3,2]

输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
使用选择排序，奇数相加时间超时；使用快速排序
'''


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = self.quict_sort(nums)
        total = 0
        for i in range(0, len(new_nums), 2):
            total += new_nums[i]
        return total

    def quict_sort(self, nums):
        if len(nums) < 2:
            return nums
        pivote = nums[0]
        less = [i for i in nums[1:] if i <= pivote]
        greater = [i for i in nums[1:] if i > pivote]
        return self.quict_sort(less) + [pivote] + self.quict_sort(greater)


if __name__ == '__main__':
    num = [1, 4, 5, 2]
    a = Solution()
    print(a.arrayPairSum(num))

# -*- coding: utf-8 -*- 
# @Time : 2019/11/4 11:11 
# @Author : 赵金林
# @Site :  
# @File : 至少是其他数字两倍的最大数.py
'''
输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.
'''
class Solution:
    def dominantIndex(self, nums):
        if len(nums) < 2:
            return 0
        new_nums = self.quick_sort(nums)
        max_num = new_nums.pop(-1)
        for i in range(0, len(new_nums)):
            if new_nums[i] == 0:
                continue
            else:
                if max_num / new_nums[i] >= 2:
                    continue
                else:
                    return -1

        for j in range(0, len(nums)):
            if nums[j] == max_num:
                return j

    def quick_sort(self, nums):
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[0]
            less = [i for i in nums[1:] if i <= pivot]
            greater = [i for i in nums[1:] if i > pivot]
            return self.quick_sort(less) + [pivot] + self.quick_sort(greater)


if __name__ == '__main__':
    nums = [1, 2, 16, 35, 44, 100, 27, 0]
    a = Solution()
    print(a.dominantIndex(nums))

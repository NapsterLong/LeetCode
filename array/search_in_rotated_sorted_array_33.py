from typing import List

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        rotate_index = self.find_rotate_index(nums)
        r1 = self.binary_search(nums, 0, rotate_index - 1, target)
        if r1 != -1:
            return r1
        return self.binary_search(nums, rotate_index, len(nums) - 1, target)

    def binary_search(self, nums, begin, end, target):
        while begin <= end:
            middle = (begin + end) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                end = middle - 1
            if nums[middle] < target:
                begin = middle + 1
        return -1

    def find_rotate_index(self, nums):
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return 0
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > nums[middle + 1]:
                return middle + 1
            if nums[middle] < nums[left]:
                right = middle - 1
            else:
                left = middle + 1


s = Solution()
print(s.search([4, 5, 1, 2, 3], 1))

from typing import List

'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) in [0, 1]:
            return len(nums)
        val = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == val:
                nums.pop(i)
            val = nums[i]
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    array = [1, 1, 2]
    s.removeDuplicates(array)
    print(array)

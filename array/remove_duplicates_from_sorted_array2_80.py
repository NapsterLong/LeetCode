from typing import List

'''
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) in [0, 1]:
            return len(nums)
        val = nums[-1]
        danger = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == val:
                if danger:
                    nums.pop(i)
                    danger = True
                else:
                    danger = True
            else:
                danger = False
            val = nums[i]
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    array = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    s.removeDuplicates(array)
    print(array)

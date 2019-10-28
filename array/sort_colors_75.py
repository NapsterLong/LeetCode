from typing import List

'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        start, end = 0, len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == 0:
                if i == start:
                    start += 1
                    continue
                else:
                    nums[i], nums[start] = nums[start], nums[i]
                    start += 1
            if nums[i] == 2:
                if i == end:
                    break
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1


if __name__ == '__main__':
    s = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    s.sortColors(nums)
    print(nums)

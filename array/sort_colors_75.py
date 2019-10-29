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
        index, start, end = 0, 0, len(nums) - 1
        while index != end:
            if nums[index] == 0:
                if start == index:
                    start += 1
                    index += 1
                    continue
                else:
                    nums[index], nums[start] = nums[start], nums[index]
                    start += 1
                    continue
            if nums[index] == 2:
                nums[index], nums[end] = nums[end], nums[index]
                end -= 1
                continue
            if nums[index] == 1:
                index += 1
                continue
        if nums[index] == 0:
            nums[index], nums[start] = nums[start], nums[index]


if __name__ == '__main__':
    s = Solution()
    nums = [2, 1]
    s.sortColors(nums)
    print(nums)

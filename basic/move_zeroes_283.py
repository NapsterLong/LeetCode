from typing import List

'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index in range(len(nums)):
            if nums[index] == 0:
                for idx2 in range(index + 1, len(nums), 1):
                    if nums[idx2] != 0:
                        nums[index], nums[idx2] = nums[idx2], nums[index]
                        break


if __name__ == '__main__':
    s = Solution()
    array = [0, 1, 0, 3, 12]
    s.moveZeroes(array)
    print(array)

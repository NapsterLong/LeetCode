'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for nums in matrix:
            if self.binary_search(nums, target):
                return True
        return False

    def binary_search(self, nums, target):
        start = 0
        end = len(nums) - 1
        middle = (end + start) // 2
        while start <= end:
            if nums[middle] == target:
                return True
            if nums[middle] > target:
                end = middle - 1
                middle = (end + start) // 2
            else:
                start = middle + 1
                middle = (end + start) // 2
        return False


if __name__ == '__main__':
    s = Solution()
    m = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(s.searchMatrix(m, 5))
    print(s.searchMatrix(m, 20))

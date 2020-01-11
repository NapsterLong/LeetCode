from typing import List

'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        result = 0
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.memo = {}
        for i in range(self.height):
            for j in range(self.width):
                result = max(self.brute_dfs(matrix, i, j), result)
        return result

    def brute_dfs(self, matrix: List[List[int]], i, j) -> int:
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        temp = []
        if i < self.height - 1 and matrix[i + 1][j] > matrix[i][j]:
            temp.append(1 + self.brute_dfs(matrix, i + 1, j))
        if i > 0 and matrix[i - 1][j] > matrix[i][j]:
            temp.append(1 + self.brute_dfs(matrix, i - 1, j))
        if j < self.width - 1 and matrix[i][j + 1] > matrix[i][j]:
            temp.append(1 + self.brute_dfs(matrix, i, j + 1))
        if j > 0 and matrix[i][j - 1] > matrix[i][j]:
            temp.append(1 + self.brute_dfs(matrix, i, j - 1))
        self.memo[(i, j)] = max(temp) if temp else 1
        return self.memo[(i, j)]


s = Solution()
print(s.longestIncreasingPath(matrix=[[13, 5, 13, 9], [5, 0, 2, 9], [10, 13, 11, 10], [0, 0, 13, 13]]))
print(s.longestIncreasingPath(matrix=[[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
print(s.longestIncreasingPath(matrix=[[1, 2]]))
print(s.longestIncreasingPath(matrix=[]))

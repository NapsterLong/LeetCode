from typing import List

'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

'''


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        self.height = len(matrix)
        self.width = len(matrix[0])
        result = 0
        for i in range(self.height):
            for j in range(self.width):
                if matrix[i][j] == "0":
                    continue
                result = max(self.maxSquare(matrix, i, j, min(self.height, self.width)), result)
        return result

    # 2-2*2-1 3 (1,0),(0,1),(1,1)
    # 3-3*3-4 5 (2,0),(2,1),(2,2),(1,2),(0,2)
    # 4-4*4-9 7
    def maxSquare(self, matrix, i, j, length):
        if i == 1 and j == 2:
            print()
        result = 1
        for l in range(2, length + 1, 1):
            y = l - 1
            flag = False
            for x in range(0, l, 1):
                if i + x < self.height and i + y < self.height and j + y < self.width and j + x < self.width and \
                        matrix[i + x][j + y] == "1" and matrix[i + y][j + x] == "1":
                    continue
                else:
                    flag = True
                    break
            if flag:
                break
            else:
                result = l * l
        return result

    def maximalSquare_dp(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        self.height = len(matrix)
        self.width = len(matrix[0])
        dp = [[0] * (self.width + 1) for _ in range(self.height + 1)]
        result = 0
        for i in range(1, self.height+1, 1):
            for j in range(1, self.width+1, 1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    result = max(result, dp[i][j])
        return result * result


s = Solution()
print(s.maximalSquare_dp(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
print(s.maximalSquare_dp([]))
print(s.maximalSquare_dp([["1"]]))

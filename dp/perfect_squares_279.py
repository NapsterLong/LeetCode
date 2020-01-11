'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''


class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        import math
        temp = int(math.sqrt(n))
        if temp * temp == n:
            return 1
        square_nums = set([i * i for i in range(1, temp + 1, 1)])
        dp = [0] * (n + 1)
        for i in range(1, n + 1, 1):
            if i in square_nums:
                dp[i] = 1
                continue
            temp_result = []
            for square in square_nums:
                if dp[i - square] != 0:
                    temp_result.append(1 + dp[i - square])
            dp[i] = min(temp_result) if temp_result else 0
        return dp[-1]


s = Solution()
print(s.numSquares(1))
print(s.numSquares(4))
print(s.numSquares(12))
print(s.numSquares(13))
print(s.numSquares(28))
print(s.numSquares(2500))

from typing import List

'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        dp = [-1] * (amount + 1)
        for idx in range(1, amount + 1, 1):
            if idx in coins:
                dp[idx] = 1
                continue
            temp = []
            for coin in coins:
                if idx < coin:
                    continue
                if dp[idx - coin] != -1:
                    temp.append(1 + dp[idx - coin])
            dp[idx] = min(temp) if temp else -1
        return dp[-1]


s = Solution()
print(s.coinChange([2], 4))

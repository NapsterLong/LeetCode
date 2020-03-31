from typing import List

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        import sys
        result = 0
        buy = sys.maxsize
        sell = None
        for idx, price in enumerate(prices):
            if sell is None:
                if price <= buy:
                    buy = price
                else:
                    sell = price
            if sell:
                if price >= sell:
                    sell = price
                    if idx == len(prices) - 1:
                        result += (sell - buy)
                else:
                    result += (sell - buy)
                    buy = price
                    sell = None
        return result

    def maxProfit2(self, prices: List[int]) -> int:
        result = 0
        for idx in range(len(prices) - 1):
            if prices[idx + 1] > prices[idx]:
                result += prices[idx + 1] - prices[idx]
        return result

    def maxProfit3(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy = prices[0]
        sell = prices[0]
        result = 0
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i + 1] <= prices[i]:
                i += 1
            begin = prices[i]
            while i < len(prices) - 1 and prices[i + 1] >= prices[i]:
                i += 1
            end = prices[i]
            result += end - begin
        return result


s = Solution()
print(s.maxProfit2([7, 1, 5, 3, 6, 4]))
# print(s.maxProfit([1, 2]))
# print(s.maxProfit([7, 6, 4, 3, 1]))

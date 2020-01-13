from typing import List

'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        result = 0
        for idx, num in enumerate(nums):
            if idx == 0:
                dp[0] = num
                result = dp[0]
                continue
            else:
                dp[idx] = max(dp[idx - 1] + num, num)
                result = max(dp[idx], result)
        return result


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4], ))

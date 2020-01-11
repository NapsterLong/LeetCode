from typing import List

'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        result = 0
        for idx, value in enumerate(nums):
            if idx == 0:
                dp[idx] = 1
                result = 1
                continue
            temp_result = 0
            for j in range(0, idx, 1):
                temp_result = max(temp_result, 1 if nums[j] >= value else dp[j] + 1)
            dp[idx] = temp_result
            result = max(result, temp_result)
        return result


s = Solution()
print(s.lengthOfLIS([4, 10, 4, 3, 8, 9]))

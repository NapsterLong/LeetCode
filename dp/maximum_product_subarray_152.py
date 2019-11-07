from typing import List

'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        import sys
        result = -sys.maxsize
        dp = [[result] * len(nums) for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i, len(nums), 1):
                if j == i:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = dp[i][j - 1] * nums[j]
                result = max(result, dp[i][j])
        return result

    def maxProduct_better(self, nums: List[int]) -> int:
        dp_max = [nums[0]] * len(nums)
        dp_min = [nums[0]] * len(nums)
        result = dp_max[0]
        for i in range(1, len(nums), 1):
            dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
            result = max(dp_max[i], result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct_better([2, 3, -2, 4]))
    print(s.maxProduct_better([-2, 0, -1]))

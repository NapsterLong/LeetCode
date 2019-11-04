from typing import List

'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        length = len(nums)
        window = length
        flag = False
        for i in range(length):
            if nums[i] >= s:
                return 1
            temp = nums[i]
            for j in range(i + 1, i + 1 + window, 1):
                if j >= length:
                    break
                if temp + nums[j] >= s:
                    window = j + 1 - i if j + 1 - i < window else window
                    flag = True
                    break
                else:
                    temp += nums[j]
            if i == 0 and not flag:
                return 0
        return window

    def minSubArrayLen_better(self, s: int, nums: List[int]) -> int:
        import sys
        ans = sys.maxsize
        left = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                ans = min(ans, i + 1 - left)
                sum -= nums[left]
                left += 1
        return ans if ans != sys.maxsize else 0


if __name__ == '__main__':
    so = Solution()
    s = 15
    nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
    print(so.minSubArrayLen_better(s, nums))

from typing import List

'''
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
Note: Length of the array will not exceed 10,000.
'''


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        last = None
        result = 0
        temp_result = 0
        for num in nums:
            if last is not None:
                if num > last:
                    temp_result += 1
                else:
                    result = max(result, temp_result)
                    temp_result = 1
            else:
                temp_result += 1
            last = num

        return max(result, temp_result)


s = Solution()
print(s.findLengthOfLCIS([1, 0, 0, 8, 6]))

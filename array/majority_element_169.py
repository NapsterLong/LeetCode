from typing import List

'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cache = {}
        for num in nums:
            cache[num] = cache.get(num, 0) + 1
            if cache[num] > int(len(nums) / 2):
                return num


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))

from typing import List

'''Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cache = {}
        for num in nums:
            if num in cache:
                cache[num] = cache[num] + 1
            else:
                cache[num] = 1
        key = [k for k, v in cache.items() if v == 1]
        return key[0]


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([4, 1, 2, 1, 2]))

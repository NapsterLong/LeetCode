from typing import List

'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        k2length = {}
        max_length = 0
        for x in nums:
            if x in k2length:
                continue
            temp = x
            temp_length = 1
            while temp + 1 in k2length or temp + 1 in nums:
                if temp + 1 in k2length:
                    temp_length += k2length[temp + 1]
                    break
                if temp + 1 in nums:
                    temp_length += 1
                temp += 1
            for i in range(x, x + temp_length, 1):
                k2length[i] = x + temp_length - i
            max_length = max(temp_length, max_length)
        return max_length


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([1, 0, -1]))

from typing import List

'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pos = set()
        neg = set()
        pos_list = []
        neg_list = []
        zeros = []
        for num in nums:
            if num > 0:
                pos.add(num)
                pos_list.append(num)
            if num < 0:
                neg.add(num)
                neg_list.append(num)
            if num == 0:
                zeros.append(0)
        result = set()
        if zeros:
            if len(zeros) >= 3:
                result.add((0, 0, 0))
            for p in pos:
                if -p in neg:
                    result.add((p, -p, 0))

        for i in range(len(pos_list)):
            for j in range(i + 1, len(pos_list), 1):
                if -(pos_list[i] + pos_list[j]) in neg:
                    result.add((pos_list[i], pos_list[j], -(pos_list[i] + pos_list[j])))
        for i in range(len(neg_list)):
            for j in range(i + 1, len(neg_list), 1):
                if -(neg_list[i] + neg_list[j]) in pos:
                    result.add((neg_list[i], neg_list[j], -(neg_list[i] + neg_list[j])))
        return [list(x) for x in result]


s = Solution()
print(s.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))

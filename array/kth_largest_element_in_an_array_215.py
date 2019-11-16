from typing import List

'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(k):
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(nums)
        return nums[-k]

    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        from heapq import nlargest
        return nlargest(k, nums)[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print(s.findKthLargest_heap([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

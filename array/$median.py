from typing import List

'''
$开头为非LeetCode的题
无序的数组的中位数。要求时间复杂度尽可能的小
'''


class Solution():
    def unsorted_array_median(self, nums: List[int]) -> float:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return sum(nums) / 2
        idx = -1
        median_idx = len(nums) // 2
        left = 0
        right = len(nums) - 1
        if len(nums) % 2 == 1:
            while idx != median_idx:
                idx = self.quick_sort(nums, left, right)
                if idx == median_idx:
                    return nums[idx]
                elif idx < median_idx:
                    left = idx + 1
                else:
                    right = idx
        else:
            value1, value2 = None, None
            while value1 is None or value2 is None:
                idx = self.quick_sort(nums, left, right)
                if idx == median_idx:
                    value2 = nums[idx]
                elif idx == median_idx - 1:
                    value1 = nums[idx]
                if idx < median_idx:
                    left = idx + 1
                else:
                    right = idx
            return (value1 + value2) / 2

    def quick_sort(self, nums, left, right):
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] >= pivot:
                right = right - 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left = left + 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left


s = Solution()
print(s.unsorted_array_median([2, 1, 3, 4, 5, 6]))
print(s.unsorted_array_median([2, 1, 3, 4, 5]))

from typing import List

'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

'''


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = self.quick_sort(nums1)
        nums2 = self.quick_sort(nums2)
        p1, p2 = 0, 0
        result = []
        while True:
            if p1 == len(nums1) or p2 == len(nums2):
                break
            if nums1[p1] < nums2[p2]:
                p1 += 1
                continue
            if nums1[p1] > nums2[p2]:
                p2 += 1
                continue
            if nums1[p1] == nums2[p2]:
                result.append(nums2[p2])
                p1 += 1
                p2 += 1
        return result

    def quick_sort(self, nums):
        if not nums or len(nums) == 1:
            return nums
        pivot = nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]

        return self.quick_sort(nums[:left]) + [pivot] + self.quick_sort(nums[right + 1:])

    def intersect_other(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = {}
        map2 = {}
        for idx, num in enumerate(nums1):
            if num not in map1:
                map1[num] = {idx}
            else:
                map1[num].add(idx)
        for idx, num in enumerate(nums2):
            if num not in map2:
                map2[num] = {idx}
            else:
                map2[num].add(idx)
        result = []
        for num in map1:
            if num not in map2:
                continue
            id_list1 = map1[num]
            id_list2 = map2[num]
            count = min(len(id_list1), len(id_list2))
            result.extend([num] * count)
        return result


s = Solution()
# print(s.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
# print(s.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
# print(s.intersect([1, 2], [1, 1]))
print(s.intersect_other([1, 2, 2, 1], [2, 2]))

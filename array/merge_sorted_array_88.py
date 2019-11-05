from typing import List

'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        idx1, idx2 = 0, 0
        stack = []
        while idx1 < m + n:
            if idx1 < m:
                if idx2 < n:
                    if nums1[idx1] <= nums2[idx2]:
                        if stack and stack[0] < nums1[idx1]:
                            stack.append(nums1[idx1])
                            nums1[idx1] = stack[0]
                            stack.pop(0)
                    if nums2[idx2] < nums1[idx1]:
                        if (stack and nums2[idx2] <= stack[0]) or (not stack):
                            stack.append(nums1[idx1])
                            nums1[idx1] = nums2[idx2]
                            idx2 += 1
                        elif stack and stack[0] < nums2[idx2]:
                            stack.append(nums1[idx1])
                            nums1[idx1] = stack[0]
                            stack.pop(0)
                else:
                    if stack:
                        stack.append(nums1[idx1])
                        nums1[idx1] = stack[0]
                        stack.pop(0)
            else:
                if idx2 < n:
                    if (stack and nums2[idx2] <= stack[0]) or (not stack):
                        nums1[idx1] = nums2[idx2]
                        idx2 += 1
                    elif stack and stack[0] < nums2[idx2]:
                        nums1[idx1] = stack[0]
                        stack.pop(0)
                else:
                    nums1[idx1] = stack[0]
                    stack.pop(0)
            idx1 += 1
            print(nums1)

    # 不考虑空间
    def merge_space(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = []
        point1 = 0
        point2 = 0
        while point1 < m or point2 < n:
            if point1 >= m:
                temp += nums2[point2:n]
                break
            if point2 >= n:
                temp += nums1[point1:m]
                break
            if nums1[point1] >= nums2[point2]:
                temp.append(nums2[point2])
                point2 += 1
            else:
                temp.append(nums1[point1])
                point1 += 1
        print(len(temp))
        nums1[:m + n] = temp


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 4, 5, 6, 0]
    nums2 = [3]
    s.merge_space(nums1, 5, nums2, 1)
    print(nums1)

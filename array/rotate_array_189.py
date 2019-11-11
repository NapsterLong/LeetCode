from typing import List

'''
Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        if k == 0:
            return
        count = 0
        for i in range(k):
            p1 = i
            p2 = (p1 + k) % len(nums)
            last = nums[p2]
            nums[p2] = nums[p1]
            p1 = p2
            count += 1
            if count == len(nums):
                return
            while i != p1:
                p2 = (p1 + k) % len(nums)
                last, nums[p2] = nums[p2], last
                p1 = p2
                count += 1
                if count == len(nums):
                    return


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2]
    s.rotate(nums, k=3)
    print(nums)

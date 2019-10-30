from typing import List

'''Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical
lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with
x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''


class Solution:
    def maxArea_brute_force(self, height: List[int]) -> int:
        max_area = 0
        length = len(height)
        for i, h1 in enumerate(height):
            if i == len(height) - 1:
                break
            if (length - i - 1) * h1 < max_area:
                continue
            for j, h2 in enumerate(height[i + 1:]):
                width = j + 1
                h = min(h1, h2)
                area = width * h
                if area > max_area:
                    max_area = area
        return max_area

    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start = 0
        end = len(height) - 1
        while start < end:
            h1 = height[start]
            h2 = height[end]
            area = min(h1, h2) * (end - start)
            if area > max_area:
                max_area = area
            if h1 < h2:
                start += 1
            else:
                end -= 1
        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

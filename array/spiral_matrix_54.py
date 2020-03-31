from typing import List

'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        height = len(matrix)
        if height == 1:
            return matrix[0]
        width = len(matrix[0])
        visited = [[0] * width for _ in range(height)]
        four = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        j = 0
        idx = 0
        current = 0
        result = []
        while idx <= width * height:
            result.append(matrix[i][j])
            idx += 1
            visited[i][j] = 1
            if idx == width * height:
                break
            next_i = i + four[current][0]
            next_j = j + four[current][1]
            while next_i >= height or next_j >= width or visited[next_i][next_j] == 1:
                current = (current + 1) % 4
                next_i = i + four[current][0]
                next_j = j + four[current][1]
            i = next_i
            j = next_j
        return result


s = Solution()
print(s.spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]))

from typing import List

'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
'''


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        result = []
        for x in matrix:
            result.extend(x)
        return heapq.nsmallest(k, result)[-1]

    def kthSmallest_binary(self, matrix: List[List[int]], k: int) -> int:
        start = matrix[0][0]
        end = matrix[-1][-1]
        while start < end:
            mid = (start + end) // 2
            count = self.find_count(matrix, mid)
            if count >= k:
                end = mid
            else:
                start = mid + 1
        return start

    def find_count(self, matrix, mid):
        count = 0
        for num1 in matrix:
            if num1[0] > mid:
                break
            for num2 in num1:
                if num2 <= mid:
                    count += 1
                else:
                    break
        return count


s = Solution()
print(s.kthSmallest_binary(matrix=[
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
],
    k=8, ))

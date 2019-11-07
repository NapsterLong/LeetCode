from typing import List

'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        matrix = [[0] * len(s) for i in range(len(s))]
        for length in range(1, len(s) + 1, 1):
            for i in range(0, len(s) - length + 1, 1):
                j = i + length - 1
                if length < 3:
                    matrix[i][j] = (s[i:j + 1], s[i] == s[j])
                else:
                    matrix[i][j] = (s[i:j + 1], s[i] == s[j] and matrix[i + 1][j - 1][1])
        stack = []
        i, j = 0, 0
        result = []
        last_flag = True
        while not (i == 0 and j == len(s) - 1):
            if j >= len(s):
                if last_flag:
                    result.append([s[0] for s in stack])
                    stack.pop(-1)
                    item = stack.pop(-1)
                else:
                    item = stack.pop(-1)
                i = item[1]
                j = item[2] + 1
                continue
            if matrix[i][j][1]:
                stack.append((matrix[i][j][0], i, j))
                i = j + 1
                j += 1
                last_flag = True
            else:
                j += 1
                last_flag = False
        if matrix[0][len(s) - 1][1]:
            result.append([s])
        return result


if __name__ == '__main__':
    s = Solution()
    # print(s.partition("a"))
    print(s.partition("efe"))
    print(s.partition("aabb"))

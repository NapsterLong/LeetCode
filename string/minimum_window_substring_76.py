'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        temp_s = []
        temp_idx = []
        for i, char in enumerate(s):
            if char in t:
                temp_s.append(char)
                temp_idx.append(i)
        if len(temp_s) < len(t):
            return ""
        result_len = -1
        result = ""
        begin, end = 0, 0
        window = {}
        while end < len(temp_s):
            if len(set(window)) < len(t):
                window.append(temp_s[end])
            while len(set(window)) == len(t):
                if temp_idx[end] - temp_idx[begin] < result_len or result_len == -1:
                    result_len = temp_idx[end] - temp_idx[begin]
                    result = s[temp_idx[begin]:temp_idx[end] + 1]
                window.pop(0)
                begin += 1
            end += 1
        return result


s = Solution()
print(s.minWindow(s="ADOBECODEBANC", t="ABC"))

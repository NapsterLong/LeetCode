'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        cache = {}
        result = 0
        for i in range(len(s)):
            if s[i] not in cache:
                cache[s[i]] = i
                result = i + 1 - start if i + 1 - start > result else result
            else:
                idx = cache[s[i]]
                start =idx + 1
                keys = [k for k, v in cache.items() if v < start]
                for key in keys:
                    cache.pop(key)
                cache[s[i]] = i
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("bbtablud"))
    print(s.lengthOfLongestSubstring("tmmzuxt"))
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))

'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cache = {}
        for idx, char in enumerate(s):
            cache[char] = cache.get(char, []) + [idx]
        result = []
        for key in cache:
            idx = cache.get(key)
            if len(idx) == 1:
                result.append(idx[0])
        return min(result) if result else -1


if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("aa"))

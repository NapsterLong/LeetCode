'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1, c2 = {}, {}
        for char in s:
            c1[char] = c1.get(char, 0) + 1
        for char in t:
            c2[char] = c2.get(char, 0) + 1
        if s == t:
            if len(c1) <= 1:
                return True
            else:
                return False
        for k, v in c1.items():
            if v != c2.get(k, -1):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram(s="anagram", t="nagaram"))
    print(s.isAnagram(s="rat", t="car"))

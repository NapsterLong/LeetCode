'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"

Output: true
Example 2:

Input: "race a car"
Output: false
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_char = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890")
        if s == "":
            return True
        start = 0
        end = len(s) - 1
        while start < end:
            char1 = s[start]
            if char1 not in valid_char:
                start += 1
                continue
            char2 = s[end]
            if char2 not in valid_char:
                end -= 1
                continue
            if self.same(char1, char2):
                start += 1
                end -= 1
                continue
            else:
                return False
        return True

    def same(self, char1, char2):
        if char1 == char2:
            return True
        if 65 <= ord(char1) <= 90:
            if ord(char2) - ord(char1) == 32:
                return True
        if 97 <= ord(char1) <= 122:
            if ord(char1) - ord(char2) == 32:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("ab"))

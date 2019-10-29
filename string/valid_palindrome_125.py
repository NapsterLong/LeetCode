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
        if s == "":
            return True
        start = 0
        end = len(s) - 1
        while start < end:
            char1 = s[start]
            if not (48 <= ord(char1) <= 57 or 65 <= ord(char1) <= 90 or 97 <= ord(char1) <= 122):
                start += 1
                continue
            char2 = s[end]
            if not (48 <= ord(char2) <= 57 or 65 <= ord(char2) <= 90 or 97 <= ord(char2) <= 122):
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

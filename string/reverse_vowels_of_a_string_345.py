'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        start = 0
        end = len(chars) - 1
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        while start < end:
            if chars[start] not in vowels:
                start += 1
                continue
            if chars[end] not in vowels:
                end -= 1
                continue
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1
        return "".join(chars)


if __name__ == '__main__':
    s = Solution()
    chars = "leetcode"
    print(s.reverseVowels(chars))

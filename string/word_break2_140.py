from typing import List

'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

'''


class Solution:
    # 自底向上,容易超出内存
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        dp = [[] for _ in range(len(s))]
        if s[0] in wordDict:
            dp[0] = [s[0]]
        else:
            dp[0] = []
        for i in range(1, len(s), 1):
            if s[0:i + 1] in wordDict:
                dp[i].append(s[0:i + 1])
            for j in range(0, i, 1):
                if dp[j] and s[j + 1:i + 1] in wordDict:
                    for v in dp[j]:
                        dp[i].append(v + " " + s[j + 1:i + 1])
        return dp[len(s) - 1]

    # 自顶向下
    def wordBreak_nb(self, s: str, wordDict: list) -> list:
        _len, wordDict = len(s), set(wordDict)
        _min, _max = 2147483647, -2147483648
        length = set([len(w) for w in wordDict])
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            res = []
            for i in length:
                if start + i < _len and s[start:start + i] in wordDict:
                    res.extend([s[start:start + i] + " " + x for x in dfs(start + i)])
                if start + i == _len and s[start:start + i] in wordDict:
                    res.extend([s[start:start + i]])
            memo[start] = res
            return res

        return dfs(0)


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak_nb(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
    print(s.wordBreak_nb(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"]))

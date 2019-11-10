from typing import List

'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

'''


class Solution:
    # 递归
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        for i in range(len(s)):
            temp = s[0:i + 1]
            if temp not in wordDict:
                continue
            else:
                if self.wordBreak(s[i + 1:], wordDict):
                    return True
        return False

    # 自底向上DP
    def wordBreak_dp(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s))
        dp[0] = s[0] in wordDict
        for i in range(1, len(s), 1):
            if s[0:i + 1] in wordDict:
                dp[i] = True
                continue
            for j in range(0, i, 1):
                if dp[j] and s[j + 1:i + 1] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s) - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak_dp(s="leetcode", wordDict=["leet", "code"]))
    print(s.wordBreak_dp(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
    print(s.wordBreak_dp(s="applepenapple", wordDict=["apple", "pen"]))

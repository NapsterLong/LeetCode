'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.memo = {}
        return self.temp(word1, word2, 0, 0)

    def temp(self, word1, word2, i, j) -> int:
        if i >= len(word1) or j >= len(word2):
            return len(word1) - i + len(word2) - j
        if word1[i] == word2[j]:
            return self.temp(word1, word2, i + 1, j + 1)
        return 1 + min(self.temp(word1, word2, i, j + 1), self.temp(word1, word2, i + 1, j),
                       self.temp(word1, word2, i + 1, j + 1))

    def dp_minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m == 0 or n == 0:
            return max(m, n)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                temp = 0 if word1[i - 1] == word2[j - 1] else 1
                dp[i][j] = min(1 + min(dp[i - 1][j], dp[i][j - 1]), temp + dp[i - 1][j - 1])
        return dp[m][n]


s = Solution()
print(s.dp_minDistance(word1="horse", word2="ros"))
print(s.dp_minDistance(word1="intention", word2="execution"))
print(s.dp_minDistance(word1="ab", word2="bc"))
print(s.dp_minDistance("dinitrophenylhydrazine", "acetylphenylhydrazine"))

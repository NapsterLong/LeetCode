from typing import List

'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. 

Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
'''


class Solution:
    # 没有DFS,结果不对
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        first_letter = set([w[0] for w in words])
        width = 0
        height = len(board)
        first2idx = {}
        for i, row in enumerate(board):
            width = len(row)
            for j, value in enumerate(row):
                if value in first_letter:
                    if value in first2idx:
                        first2idx[value].append((i, j))
                    else:
                        first2idx[value] = [(i, j)]
        result = []
        for word in words:
            if word[0] not in first2idx:
                continue
            for i, j in first2idx[word[0]]:
                flag2 = False
                for w in word[1:]:
                    up = board[i - 1][j] if i - 1 >= 0 else ""
                    if w == up:
                        i = i - 1
                        continue
                    down = board[i + 1][j] if i + 1 < height else ""
                    if w == down:
                        i = i + 1
                        continue
                    left = board[i][j - 1] if j - 1 >= 0 else ""
                    if w == left:
                        j = j - 1
                        continue
                    right = board[i][j + 1] if j + 1 < width else ""
                    if w == right:
                        j = j + 1
                        continue
                    flag2 = True
                    break
                if not flag2:
                    result.append(word)
                    break
        return result

    def findWords_better(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i, j, t, s):
            ch = board[i][j]
            if ch not in t:
                return
            t = t[ch]
            if "end" in t and t["end"] == 1:
                res.append(s + ch)
                t["end"] = 0
            board[i][j] = "#"
            if i + 1 < m and board[i + 1][j] != "#":
                dfs(i + 1, j, t, s + ch)
            if i - 1 >= 0 and board[i - 1][j] != "#":
                dfs(i - 1, j, t, s + ch)
            if j + 1 < n and board[i][j + 1] != "#":
                dfs(i, j + 1, t, s + ch)
            if j - 1 >= 0 and board[i][j - 1] != "#":
                dfs(i, j - 1, t, s + ch)
            board[i][j] = ch

        # 将word存入前缀树
        trie = {}
        for word in words:
            t = trie
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t["end"] = 1

        m = len(board)
        n = len(board[0])
        res = []
        # 对board进行深度优先搜索
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "")
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findWords_better(board=[
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ],
        words=["oath", "pea", "eat", "rain"]))

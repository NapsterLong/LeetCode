from typing import List

'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        Q = [root]
        result = []
        index = 0
        while Q:
            temp = []
            temp_result = []
            while Q:
                value = Q.pop(0)
                temp_result.append(value.val)
                if value.left:
                    temp.append(value.left)
                if value.right:
                    temp.append(value.right)
            index += 1
            if index % 2 == 1:
                result.append(temp_result)
            else:
                result.append(list(reversed(temp_result)))
            for t in temp:
                Q.append(t)
        return result

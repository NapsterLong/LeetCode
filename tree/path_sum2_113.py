from typing import List

'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return None
        return list(filter(None, self.pathSumR(root, sum, [])))

    def pathSumR(self, root: TreeNode, sum: int, temp: List[int]):
        if root is None:
            return [None]
        if root.left is None and root.right is None and root.val == sum:
            return [temp + [root.val]]
        left = self.pathSumR(root.left, sum - root.val, temp + [root.val])
        right = self.pathSumR(root.right, sum - root.val, temp + [root.val])
        return left + right

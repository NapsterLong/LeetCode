from typing import List

'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        result = self.binaryTreePathsR(root, [])
        return ["->".join(r) for r in result]

    def binaryTreePathsR(self, root: TreeNode, last: List[str]):
        if root.left is None and root.right is None:
            return [last + [str(root.val)]]
        left = self.binaryTreePathsR(root.left, last + [str(root.val)]) if root.left else []
        right = self.binaryTreePathsR(root.right, last + [str(root.val)]) if root.right else []
        return left + right

    def binaryTreePathsS(self, root: TreeNode) -> List[str]:
        pass

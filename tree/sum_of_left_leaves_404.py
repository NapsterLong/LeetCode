'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.sumOfLeftLeavesR(root, True)

    def sumOfLeftLeavesR(self, root: TreeNode, is_left: bool) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None and is_left:
            return root.val
        left = self.sumOfLeftLeavesR(root.left, True)
        right = self.sumOfLeftLeavesR(root.right, False)
        return left + right

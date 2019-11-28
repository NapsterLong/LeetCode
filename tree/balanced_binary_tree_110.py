'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedR(root)[1]

    def isBalancedR(self, root: TreeNode):
        if root is None:
            return 0, True
        left_d, left = self.isBalancedR(root.left)
        if not left:
            return None, False
        right_d, right = self.isBalancedR(root.right)
        if not right:
            return None, False
        return max(left_d, right_d) + 1, abs(left_d - right_d) <= 1

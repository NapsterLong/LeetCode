'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        tra = self.traversal(root)
        for i in range(len(tra) - 1):
            if tra[i] >= tra[i + 1]:
                return False
        return True

    def traversal(self, root: TreeNode):
        if root is None:
            return []
        left = self.traversal(root.left) if root.left else []
        right = self.traversal(root.right) if root.right else []
        return left + [root.val] + right

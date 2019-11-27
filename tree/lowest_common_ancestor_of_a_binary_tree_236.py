'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [(root, [root])]
        path1, path2 = [], []
        while stack:
            node, path = stack.pop(0)
            if node == p:
                path1 = path
            if node == q:
                path2 = path
            if path1 and path2:
                break
            if node.left:
                temp = path[:]
                temp.append(node.left)
                stack.append((node.left, temp))
            if node.right:
                temp = path[:]
                temp.append(node.right)
                stack.append((node.right, temp))
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[-1 - i] in path2:
                return path1[-1 - i]
            if path2[-1 - i] in path1:
                return path2[-1 - i]
            i += 1
        return None

    def lowestCommonAncestorR(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestorR(root.left, p, q)
        right = self.lowestCommonAncestorR(root.right, p, q)
        if left and right:
            return root
        return left if left is not None else right

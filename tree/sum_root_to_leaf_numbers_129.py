'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.sumNumbersR(root, [])

    def sumNumbersR(self, root: TreeNode, parent) -> int:
        if root.left is None and root.right is None:
            value = root.val
            for i in range(len(parent)):
                value += 10 ** (i + 1) * parent[-1 - i]
            return value
        temp = parent[:]
        temp.append(root.val)
        left = self.sumNumbersR(root.left, temp) if root.left else 0
        right = self.sumNumbersR(root.right, temp) if root.right else 0
        return left + right

'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [root]
        while stack:
            temp_result = []
            temp_stack = []
            for s in stack:
                temp_result.append(s.val if s else None)
                if s:
                    temp_stack.append(s.left)
                    temp_stack.append(s.right)
            for i in range(len(temp_result) // 2):
                if temp_result[i] != temp_result[-i - 1]:
                    return False
            stack = temp_stack[:]
        return True

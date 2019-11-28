'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
        return self.pathSumR(root, sum, [])

    def pathSumR(self, root: TreeNode, sum: int, parent) -> int:
        if root.left is None and root.right is None:
            count = 0 if root.val != sum else 1
            temp_s = root.val
            for i in range(len(parent)):
                temp_s += parent[-i - 1]
                if temp_s == sum:
                    count += 1
        temp = parent[:]
        temp.append(root.val)
        left = self.pathSumR(root.left, sum, temp) if root.left else 0
        right = self.pathSumR(root.right, sum, temp) if root.right else 0
        count, temp_s = 0, 0
        for i in range(len(temp)):
            temp_s += temp[-i - 1]
            if temp_s == sum:
                count += 1
        return left + right + count

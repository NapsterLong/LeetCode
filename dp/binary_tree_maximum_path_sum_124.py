'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        import sys
        if root is None:
            return 0
        self.node2sum = {}
        self.max_sum = -sys.maxsize
        self.pathSumDown(root)
        print(self.node2sum)
        self.maxPathSuR(root, None, None)
        return self.max_sum

    def pathSumDown(self, root: TreeNode):
        leftSum = self.pathSumDown(root.left) if root.left else 0
        rightSum = self.pathSumDown(root.right) if root.right else 0
        self.node2sum[root] = {"left": leftSum + root.val, "right": rightSum + root.val}
        return max(leftSum, rightSum) + root.val

    def maxPathSuR(self, root: TreeNode, source, parent):
        if root is None:
            return
        if source is None:
            self.max_sum = max(root.val, self.node2sum[root]["left"], self.node2sum[root]["right"], self.max_sum)
            self.node2sum[root]["up"] = 0
        if source == "left":
            self.max_sum = max(root.val, self.node2sum[root]["left"], self.node2sum[root]["right"],
                               root.val + self.node2sum[parent]["right"], root.val + self.node2sum[parent]["up"],
                               self.max_sum)
            self.node2sum[root]["up"] = max(root.val + self.node2sum[parent]["up"], root.val + parent.val,
                                            root.val + self.node2sum[parent]["right"])
        if source == "right":
            self.max_sum = max(root.val, self.node2sum[root]["left"], self.node2sum[root]["right"],
                               root.val + self.node2sum[parent]["left"], root.val + self.node2sum[parent]["up"],
                               self.max_sum)
            self.node2sum[root]["up"] = max(root.val + self.node2sum[parent]["up"], root.val + parent.val,
                                            root.val + self.node2sum[parent]["left"])
        self.maxPathSuR(root.left, "left", root)
        self.maxPathSuR(root.right, "right", root)

# [5,4,8,11,null,13,4,7,2,null,null,null,1]
s = Solution()
t = TreeNode(2)
t.left = TreeNode(-1)
t.right = TreeNode(-2)
print(s.maxPathSum(t))

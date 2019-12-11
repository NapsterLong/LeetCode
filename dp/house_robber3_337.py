from typing import List

'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        nums = self.levelOrder(root)
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                dp[i] = num
            elif i == 1:
                dp[i] = max(num, nums[0])
            else:
                dp[i] = max(dp[i - 2] + num, dp[i - 1])
        return dp[-1] if dp else 0

    def levelOrder(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        stack = [root]
        while stack:
            length = len(stack)
            for t in stack:
                if t.left:
                    stack.append(t.left)
                if t.right:
                    stack.append(t.right)
            temp_result = 0
            for i in range(length):
                x = stack.pop(i)
                temp_result += x.val
            result.append(temp_result)
        return result

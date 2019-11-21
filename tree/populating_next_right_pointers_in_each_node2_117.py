'''
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


Example:

Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}

Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
 
Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.

'''


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if root is None:
            return root
        self.connectR(root, None)
        return root

    def connectR(self, root: Node, p):
        root.next = p
        left_p = None
        right_p = None
        first = None
        temp = root.next
        while temp:
            if temp.left:
                first = temp.left
                break
            if temp.right:
                first = temp.right
                break
            temp = temp.next
        left_p = root.right if root.right else first
        right_p = first

        if root.left:
            self.connectR(root.left, left_p)
        if root.right:
            self.connectR(root.right, right_p)

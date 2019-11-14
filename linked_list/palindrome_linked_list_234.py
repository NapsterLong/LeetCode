'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        for idx in range(len(temp) // 2):
            if temp[idx] == temp[-(idx + 1)]:
                continue
            else:
                return False
        return True

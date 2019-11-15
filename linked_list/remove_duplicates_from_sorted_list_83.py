'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        last = head
        ptr = head.next
        flag = False
        while ptr:
            if ptr.val == last.val:
                ptr = ptr.next
                flag = True
            else:
                if flag:
                    last.next = ptr
                    last = ptr
                    ptr = ptr.next
                else:
                    last = last.next
                    ptr = ptr.next
        if flag:
            last.next=None
        return head

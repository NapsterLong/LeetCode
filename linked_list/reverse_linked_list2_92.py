'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_string(self):
        result = [self.val]
        next = self.next
        while next:
            result.append(next.val)
            next = next.next
        print("->".join([str(x) for x in result]))


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head.next is None:
            return head
        index = 1
        ptr = head
        start = head if m != 1 else ListNode(0)
        last = start
        while ptr:
            if index <= m - 1:
                start = ptr
                last = ptr
                ptr = ptr.next
            if index == m:
                temp = ptr.next
                ptr.next = None
                start.next = ptr
                last = ptr
                ptr = temp
            if m < index <= n:
                temp = ptr.next
                ptr.next = start.next
                start.next = ptr
                ptr = temp
            if index > n:
                last.next = ptr
                break
            index += 1
        return head if m != 1 else start.next


s = Solution()
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
a.to_string()
s.reverseBetween(a, 2, 5).to_string()

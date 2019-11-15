'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        import sys
        mute = ListNode(0)
        ptr = head
        last_ptr = mute
        last_val = sys.maxsize
        while ptr and ptr.next:
            if ptr.val != last_val and ptr.val != ptr.next.val:
                last_ptr.next = ptr
                last_ptr = ptr
            last_val = ptr.val
            ptr = ptr.next
        if ptr.val == last_val:
            last_ptr.next = None
        else:
            last_ptr.next = ptr
        return mute.next

s = Solution()
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(3)
a.next.next.next.next = ListNode(4)
a.next.next.next.next.next = ListNode(4)
a.next.next.next.next.next.next = ListNode(5)
a.to_string()
s.deleteDuplicates(a).to_string()
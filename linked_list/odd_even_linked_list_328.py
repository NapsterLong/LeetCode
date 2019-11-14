'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        odd = None
        even = None
        ptr_odd, ptr_even = head, head.next
        while ptr_odd is not None or ptr_even is not None:
            if ptr_odd is not None:
                temp_odd = ptr_odd.next.next if ptr_odd.next else None
                if odd is None:
                    ptr_odd.next = None
                    odd = ptr_odd
                else:
                    ptr_odd.next = odd.next
                    odd.next = ptr_odd
                    odd = odd.next
                ptr_odd = temp_odd

            if ptr_even is not None:
                temp_even = ptr_even.next.next if ptr_even.next else None
                ptr_even.next = None
                if even is None:
                    even = ptr_even
                    odd.next = even
                else:
                    even.next = ptr_even
                    even = even.next
                ptr_even = temp_even
        return head

'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

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
    def sortList(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head
        ptr = head
        new = None
        while ptr:
            if new is None:
                record = ptr.next
                new = ptr
                new.next = None
                ptr = record
                continue
            if ptr.val < new.val:
                temp = ptr.next
                ptr.next = new
                new = ptr
                ptr = temp
                continue
            record = new
            temp = new
            while temp:
                if temp.val <= ptr.val:
                    if temp.next is None:
                        temp2 = ptr.next
                        temp.next = ptr
                        temp.next.next = None
                        ptr = temp2
                        new = record
                        break
                    if temp.next.val >= ptr.val:
                        temp2 = ptr.next
                        ptr.next = temp.next
                        temp.next = ptr
                        ptr = temp2
                        new = record
                        break
                    temp = temp.next
        return new


s = Solution()
node1 = ListNode(4)
node1.next = ListNode(2)
node1.next.next = ListNode(1)
node1.next.next.next = ListNode(3)
node1.to_string()
s.sortList(node1).to_string()

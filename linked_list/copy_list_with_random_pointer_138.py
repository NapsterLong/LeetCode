'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:

You must return the copy of the given head as a reference to the cloned list.

'''


# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if head is None:
            return None
        old_node = head
        new_node = Node(old_node.val, None, None)
        visited = {old_node: new_node}
        while old_node is not None:
            if old_node.random:
                if old_node.random not in visited:
                    visited[old_node.random] = Node(old_node.random.val, None, None)
                new_node.random = visited[old_node.random]
            else:
                new_node.random = None
            if old_node.next:
                if old_node.next not in visited:
                    visited[old_node.next] = Node(old_node.next.val, None, None)
                new_node.next = visited[old_node.next]
            else:
                new_node.next = None
            old_node = old_node.next
            new_node = new_node.next
        return visited[head]

    def copyRandomList_O1(self, head: Node) -> Node:
        if head is None:
            return None
        ptr = head
        # A A' B B' C C'
        while ptr:
            new_node = Node(ptr.val, None, None)
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
        ptr_old = head
        ptr_new = head.next
        head_old = head.next
        while ptr_old:
            ptr_old.next = ptr_old.next.next
            ptr_new.next = ptr_new.next.next if ptr_new.next else None
            ptr_old = ptr_old.next
            ptr_new = ptr_new.next
        return head_old

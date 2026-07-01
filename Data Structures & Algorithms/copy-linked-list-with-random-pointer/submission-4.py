"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # lets handle a quick edge case 
        dummy = Node(0)
        tail = dummy 
        curr = head 
        old_to_new = {}

        while curr:
            new_node = Node(curr.val)
            tail.next = new_node 
            old_to_new[curr] = new_node
            tail = tail.next 
            curr = curr.next 

        old_to_new[None] = None

        curr = head 
        new_curr = dummy.next 

        while curr:
            new_curr.random = old_to_new[curr.random]
            new_curr = new_curr.next 
            curr = curr.next

        return dummy.next

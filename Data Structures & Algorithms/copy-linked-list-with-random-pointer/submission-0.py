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
        # init 
        dummy = Node(0)
        tail = dummy 
        curr = head 
        old_to_new = {}
        # first pass: creata a copy of the list and a refference map
        while curr: 
            new_node = Node(curr.val)
            tail.next = new_node
            old_to_new[curr] = new_node 
            tail = tail.next
            curr = curr.next 
        # add a none element in refference map
        old_to_new[None] = None 
        # second pass: wire up the random pointers 
        curr = head
        new_curr = dummy.next

        while curr: 
            new_curr.random = old_to_new[curr.random]
            new_curr = new_curr.next 
            curr = curr.next 

        return dummy.next
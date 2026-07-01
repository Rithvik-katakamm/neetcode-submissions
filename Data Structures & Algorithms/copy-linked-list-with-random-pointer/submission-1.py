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
        if not head:
            return None
        # init dummy, tail and old to new hashy 
        dummy = Node(0)
        tail = dummy 
        old_to_new = {}
        curr = head 
        # walk through the original list
        while curr:
            # create a copy and map old nodes to new
            new_node = Node(curr.val)
            tail.next = new_node # wiring up next 
            old_to_new[curr] = new_node\
            # advance the pointets 
            tail = tail.next
            curr = curr.next  
        # set the hashy's None value to none to avoid edge cases
        old_to_new[None] = None  
        # walk through the original list again 
        curr = head 
        new_curr = dummy.next 
        while curr:
            # wire up random 
            new_curr.random = old_to_new[curr.random]
            new_curr = new_curr.next 
            curr = curr.next
        # return the tail of dummy
        return dummy.next 


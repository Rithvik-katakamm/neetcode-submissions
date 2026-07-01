# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        ''' fast and slow pointer '''

        # code 
        # init a set 
        seen = set()
        curr = head 
        # loop through the linked list 
        while curr:
            # ask if we have seen this node before 
            if curr in seen:
                # return true
                return True 
            # add the node to seen
            seen.add(curr)
            curr = curr.next 
        # return false
        return False 
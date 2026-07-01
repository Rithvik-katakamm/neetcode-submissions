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
        # loop through the linked list 
        while head:
            # ask if we have seen this node before 
            if head in seen:
                # return true
                return True 
            # add the node to seen
            seen.add(head)
            head = head.next 
        # return false
        return False 
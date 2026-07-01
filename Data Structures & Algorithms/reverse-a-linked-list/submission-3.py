# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # code 
        # set prev and current 
        previous = None 
        current = head 

        # while current is still valid 
        while current:
            # cache what's next 
            nxt = current.next 
            # flip the pointer pointing to next
            current.next = previous 
            # update prev and current 
            previous = current 
            current =  nxt 
        # return the new head
        return previous  
        
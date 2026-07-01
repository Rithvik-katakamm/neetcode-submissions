# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # code 
        # set previous and current 
        previous = None 
        current = head 
        # while current is stil valid
        while current:
            # set next
            nxt = current.next
            # flip the pointer
            current.next = previous 
            # move prev and curr
            previous = current
            current = nxt
        # return new headv
        return previous
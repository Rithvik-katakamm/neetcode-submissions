# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # code 
        # set prev and curr
        prev = None
        curr = head 
        # while curr is not none
        while curr: 
            # cache the next pointer
            nxt = curr.next 
            # flip pointer to prev
            curr.next = prev 
            # move both prev and curr
            prev = curr
            curr = nxt 
        # return prev as its the new head
        return prev
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # code 
        # init prev and current 
        prev = None 
        curr = head 
        # while current is not None
        while curr:
            # cache the next node
            nxt = curr.next 
            # flip curr pointer to prev
            curr.next = prev 
            # advance prev and curr
            prev = curr
            curr = nxt
        # return prev
        return prev 
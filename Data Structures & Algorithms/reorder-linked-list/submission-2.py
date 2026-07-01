# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # code 
        # find the middle (slow fast pointer)
        slow, fast, slow = head, head, head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        second = slow.next # this is the second head 
        slow.next = None # cut that shit by the knees 

        # reverse the second half of the list 
        prev = None 
        curr = second

        while curr:
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt 
        
        second = prev # new head 
        # weave
        first = head

        while second:
            temp1, temp2 = first.next, second.next 

            first.next = second 
            second.next = temp1 

            second = temp2
            first = temp1

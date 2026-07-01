# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # target complexity: time -> O(n), space -> O(1)

        # code 
        # find the middle 
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        second = slow.next # head of the second half 
        slow.next = None # cut the cord 

        # reverse the second half of the list 
        prev = None 
        curr = second 

        while curr:
            # cache next
            nxt = curr.next 
            curr.next = prev 
            # advacne both forward 
            prev = curr 
            curr = nxt

        second = prev # new head of second half 
        # weave them together 
        first = head 
        while second:
            temp1, temp2 = first.next, second.next 

            first.next = second 
            second.next = temp1 
            
            first, second = temp1, temp2 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # code 
        # split the list down the middle 
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        second = slow.next 
        slow.next = None # sever the connection 
        # rev the list
        prev = None 
        curr = second 

        while curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt

        # weave 
        first, second = head, prev 

        while second:
            temp1, temp2 = first.next, second.next
            
            first.next = second
            second.next = temp1

            first, second = temp1, temp2
        
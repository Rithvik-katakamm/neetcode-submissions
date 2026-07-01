# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # understand 
        # input: head -> node (Linked list)
        # modify the nodes to be in [0, n-1, 1, n-2, 2, n-3, ...] order
        # expected return: reordered list
        # seems like the expected time is O(n) and space is O(1) 
        # this tells me this is a pointer ordeal 

        # code 
        # find the middle, split the list 
        slow = head; fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        middle = slow.next # new head for the second list
        slow.next = None 
        # reverse the second half 
        prev = None 
        curr = middle

        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr # new head 
            curr = nxt 
        
        second = prev  
        # weaave them together
        first = head 

        while second:
            temp1 = first.next 
            first.next = second

            temp2 = second.next 
            second.next = temp1 

            first = temp1 
            second = temp2 

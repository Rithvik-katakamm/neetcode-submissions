# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy, init 
        dummy = ListNode()
        tail = dummy 
        carry = 0 
        # while any
        while l1 or l2 or carry:
            # assign digits 
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            # calc total, quotient and remainder
            total = d1 + d2 + carry 
            carry = total // 10 
            digit = total % 10
            # create new node with remain 
            tail.next = ListNode(digit)
            tail = tail.next 
            # move the heads of the lits
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 
        # return the new head 
        return dummy.next 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # if the head or head;s next pointer is none return false
        if not head or not head.next: 
            return False 
        # init the pointers 
        slow, fast = head, head 
        # move through the list while fast and fast.next are valid
        while fast and fast.next:
            # bump thw slow pointer
            slow = slow.next
            fast = fast.next.next  
            # if fast and slow are equal
            if fast == slow:
                return True  
        # return false 
        return False 
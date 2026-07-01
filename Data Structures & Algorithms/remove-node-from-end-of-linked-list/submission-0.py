# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # understand:
        # input ex: [1,2,3,4], n = 2. 
        # expected output: [1,2,4]
        # need to remove the nth node from the back 
        # which is 3 here in our example 

        ''' slow and fast pointer ''' 

        # init slow and fast at head 
        dummy = ListNode(0,head)
        slow, fast = dummy, dummy
        # advance fast about n + 1 nodes ahead of slow 
        for i in range(n+1):
            fast = fast.next 
        # advance both pointers till fast hits the end
        while fast:
            slow = slow.next 
            fast = fast.next 
        # then re wire slows next pointer to skip the nth node 
        slow.next = slow.next.next 
        # return head
        return dummy.next
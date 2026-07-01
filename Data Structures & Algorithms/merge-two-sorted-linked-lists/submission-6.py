# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # understand 
        # input: list1, list2 -> node head 
        # expected output: head of new sorted aray 
        
        # code 
        dummy = ListNode()
        tail = dummy
        # now compare the values of the heads of both lists 
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next
            
            # advace tail forward 
            tail = tail.next 

        tail.next = list1 if list1 else list2

        # return the head 
        return dummy.next

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ''' linked list '''

        # code 
        # create a dummy node 
        dummy = ListNode()      
        # assign tail 
        tail = dummy 
        # while list1 and list2 are not nothing 
        while list1 and list2:
            # if list1 val is less than or equal to list2 val 
            if list1.val <= list2.val:
                # tail's next pointer is list1
                tail.next = list1
                # list1 becomes the next node in the list
                list1 = list1.next 
            # else
            else:
                # tails next pointer is list 2
                tail.next = list2 
                # list2 is the next node in list2
                list2 = list2.next 
            # update tail 
            tail = tail.next

        # id there are any left append it to the end of the list 
        tail.next = list1 if list1 else list2
        # return 
        return dummy.next
            
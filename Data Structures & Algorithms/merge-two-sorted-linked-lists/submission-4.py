# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ''' linked list '''

        # code
        dummy = ListNode()
        tail = dummy 

        # while list1 and list2 are valid 
        while list1 and list2:
            # if list1 is less than or equal to list2
            if list1.val <= list2.val:
                # attach the tail to list one
                tail.next = list1 
                # advance list 1 head
                list1 = list1.next 
            # else
            else:
                # attach the tail to list2
                tail.next = list2
                # advance list2
                list2 = list2.next 
            tail = tail.next 
        # if there are any numbers left attach them too
        tail.next = list1 if list1 else list2
        # return dummy tail 
        return dummy.next 
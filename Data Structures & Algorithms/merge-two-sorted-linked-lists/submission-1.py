# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ''' linked list '''

        # code 
        # create a dummy node and assign tail as another way to refference it 
        dummy = ListNode()
        tail = dummy 
        # while list1 and 2 have values 
        while list1 and list2:
            # is list1(head) less than or equal to list2?
            if list1.val <= list2.val:
                # attach it as tails next pointer 
                tail.next = list1
                # advance list1
                list1 = list1.next 
            # if not
            else:
                # attach tail's next pointer to list2
                tail.next = list2
                # advance list2
                list2 = list2.next
            # advance tail
            tail = tail.next 
        # if there are values still left attach them to tail 
        tail.next = list1 if list1 else list2
        # return 
        return dummy.next
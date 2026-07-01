# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # understand 
        # input: list1, list2 -> node head 
        # expected output: head of new sorted array. 

        # code
        # set a dummy node to start from, gice it alternate ref, tail.
        dummy = ListNode()
        tail = dummy 
        # while list1 and list2 are valid
        while list1 and list2:
            # compare the values
            if list1.val <= list2.val: 
                # attached smaller value to the tail and advance 
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # advance tail forward
            tail = tail.next
        # attach the tail to the remaining head 
        tail.next = list1 if list1 else list2
        # return whatever points to the head of the first node 
        return dummy.next
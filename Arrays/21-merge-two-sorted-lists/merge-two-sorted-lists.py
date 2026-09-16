# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Starting point for the result
        current = dummy  # Points to the last node in the result
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1  # Take the smaller node from list1
                list1 = list1.next  # Move list1 forward
            else:
                current.next = list2  # Take the smaller node from list2
                list2 = list2.next  # Move list2 forward
            current = current.next  # Move result pointer forward
        if list1:
            current.next = list1  # Attach remaining list1 nodes
        else:
            current.next = list2  # Attach remaining list2 nodes
        return dummy.next  # Skip dummy and return the actual result
        
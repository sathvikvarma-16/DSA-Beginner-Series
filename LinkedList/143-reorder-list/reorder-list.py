# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        # Find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Second list starts after middle
        second = slow.next
        slow.next = None
        # Reverse second list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # First list
        first = head
        # Add one from first, one from reversed second
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2


"""
# 1,2,3,4,5
first:   1 → 2 → 3
second:  5 → 4

output : 1 5 2 4 3

first = head             # first = 1
second = prev            # second = 5 
while second:            # Continue while second has nodes
    temp1 = first.next   # Save 2
    temp2 = second.next  # Save 4

    first.next = second  # 1 → 5
    second.next = temp1  # 5 → 2

    first = temp1        # Move first to 2
    second = temp2       # Move second to 4
"""


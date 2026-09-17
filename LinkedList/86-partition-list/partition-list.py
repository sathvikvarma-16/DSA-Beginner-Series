# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        small = ListNode(0)       # Dummy for nodes smaller than x
        large = ListNode(0)       # Dummy for nodes >= x
        s = small                 # Pointer for small list
        l = large                 # Pointer for large list
        while head:
            if head.val < x:      # If value is smaller than x
                s.next = head     # Add it to small list
                s = s.next        # Move small pointer
            else:                 # If value is >= x
                l.next = head     # Add it to large list
                l = l.next        # Move large pointer
            head = head.next      # Move to next original node
        l.next = None             # End the large list
        s.next = large.next       # Connect small list to large list
        return small.next         # Return actual beginning

        
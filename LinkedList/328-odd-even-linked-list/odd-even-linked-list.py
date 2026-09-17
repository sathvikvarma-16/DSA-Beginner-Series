# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:       # If 0 or 1 node, return as it is
            return head
        odd = head                            # odd points to 1st node
        even = head.next                      # even points to 2nd node
        even_head = even                     # Remember where even list starts
        while even and even.next:            # Continue while odd/even nodes exist
            odd.next = even.next             # Connect odd node to next odd node
            odd = odd.next                   # Move odd pointer forward
            even.next = odd.next             # Connect even node to next even node
            even = even.next                 # Move even pointer forward
        odd.next = even_head                 # Attach even list after odd list
        return head           
        
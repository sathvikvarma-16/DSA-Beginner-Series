# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:   # Nothing to rotate
            return head
        last = head                                   # Start from head
        length = 1                                    # Count nodes
        while last.next:                              # Go until last node
            last = last.next                          # Move forward
            length += 1                               # Count node
        k = k % length                                # Remove unnecessary full rotations
        if k == 0:                                    # No rotation needed
            return head
        last.next = head                              # Make list circular
        new_last = head                               # Find new last node
        for i in range(length - k - 1):               # Move to new last node
            new_last = new_last.next
        new_head = new_last.next                      # Next node becomes new head
        new_last.next = None                          # Break the circle
        return new_head   

        
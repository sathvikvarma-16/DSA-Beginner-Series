# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Dummy node before head
        dummy = ListNode(0)
        dummy.next = head
        # Both start at dummy
        slow = dummy
        fast = dummy
        # Move fast n+1 steps ahead
        for i in range(n + 1):
            fast = fast.next
        # Move both until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
        # Remove the node
        slow.next = slow.next.next
        # Return the actual head
        return dummy.next
        
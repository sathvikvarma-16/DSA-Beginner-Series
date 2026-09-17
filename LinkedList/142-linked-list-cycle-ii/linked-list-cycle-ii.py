# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow moves 1 step
        # fast moves 2 steps
        slow = head
        fast = head
        # Keep moving while fast has nodes to move through
        while fast and fast.next:
            # Move slow by 1
            slow = slow.next
            # Move fast by 2
            fast = fast.next.next
            # If they meet, a cycle exists
            if slow == fast:
                break
        # If fast reached the end, there is NO cycle
        else:
            return None

        # Cycle exists
        # Move slow back to the beginning
        slow = head
        # Now move BOTH one step at a time
        while slow != fast:
            slow = slow.next
            fast = fast.next
        # They meet at the START of the cycle
        return slow
        
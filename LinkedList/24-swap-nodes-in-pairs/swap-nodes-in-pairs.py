# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            first = current.next          # First node of the pair
            second = current.next.next    # Second node of the pair
            first.next = second.next      # First points to the node after second
            second.next = first           # Second points to first → swap happens
            current.next = second         # Connect previous part to second => But dummy is still pointing to first.next in 1st iteration, so we haven't connected the previous part correctly yet.
            current = first               # Move current to first for the next pair => first is 1. So current moves to 1 in first iteration for further swapping
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)             # Temporary starting node
        current = dummy                 # Pointer to build the answer list
        carry = 0                       # Stores carry from previous addition
        while l1 or l2 or carry:        # Continue while nodes or carry remain
            x = l1.val if l1 else 0     # Get l1 value, or 0 if l1 is empty
            y = l2.val if l2 else 0     # Get l2 value, or 0 if l2 is empty
            total = x + y + carry       # Add both digits and carry
            carry = total // 10         # Get carry for next position
            digit = total % 10          # Get current digit
            current.next = ListNode(digit)  # Create node with current digit
            current = current.next          # Move current to the new node
            if l1:                          # If l1 still has nodes
                l1 = l1.next                # Move l1 to the next node
            if l2:                          # If l2 still has nodes
                l2 = l2.next                # Move l2 to the next node
        return dummy.next                   # Return the actual answer list


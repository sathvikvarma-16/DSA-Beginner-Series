# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(0)              # Temporary node
        dummy.next = head                 # Connect dummy to head
        prev = dummy                      # Move to node before left
        for i in range(left - 1):
            prev = prev.next              # Move prev forward
        current = prev.next               # First node to reverse
        for i in range(right - left):
            temp = current.next           # Save next node
            current.next = temp.next      # Remove temp from its position
            temp.next = prev.next         # Put temp at the front
            prev.next = temp              # Connect prev to temp
        return dummy.next                 # return the new head


"""
For 1 → 2 → 3 → 4 → 5, reverse positions 2 to 4.
left=2, right=4

Steps simply:
Find the node before left → prev = 1
Keep current at the first node to reverse → current = 2
Take the node after current → temp = 3
Remove temp from its current position
Put temp before current
Repeat until we reach right
Now the reversed part is 4 → 3 → 2
Return the original head using dummy.next

So the main idea is:

Take the next node → remove it → put it at the front → repeat.
"""


"""
for 1,2,3,4,5,6
left = 2, right=5
output : 1,5,4,3,2,6
"""
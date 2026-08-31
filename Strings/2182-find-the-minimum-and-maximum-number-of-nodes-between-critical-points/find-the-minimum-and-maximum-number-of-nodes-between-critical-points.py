# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical = []
        
        prev = head
        curr = head.next
        pos = 1
        while curr.next:
            # Check if curr is a critical point
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                critical.append(pos)
            prev = curr
            curr = curr.next
            pos += 1
        # Fewer than 2 critical points
        if len(critical) < 2:
            return [-1, -1]
        # Minimum distance between consecutive critical points
        min_dist = float('inf')
        for i in range(1, len(critical)):
            min_dist = min(min_dist, critical[i] - critical[i - 1])
        # Maximum distance between first and last
        max_dist = critical[-1] - critical[0]
        return [min_dist, max_dist]
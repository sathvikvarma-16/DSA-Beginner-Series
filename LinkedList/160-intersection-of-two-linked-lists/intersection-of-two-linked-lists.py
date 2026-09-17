# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        while a != b:
            if a:
                a = a.next
            else:
                a = headB
            if b:
                b = b.next
            else:
                b = headA
        return a


        """
        a travels: List A + List B
        b travels: List B + List A

Therefore, if an intersection exists, they meet at the intersection node. If there is no intersection, both eventually become None and the loop stops.
"""
# Input  =     4 -> 1 -> 8 -> 4 -> 5
#           5 -> 6 -> 1 /

# Output = 8 


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        p1, p2 = headA, headB

        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p2

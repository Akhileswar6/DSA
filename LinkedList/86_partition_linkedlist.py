# Input  = 1 -> 4 -> 3 -> 2 -> 5 -> 2,  x = 3
# Output = 1 -> 2 -> 2 -> 4 -> 3 -> 5

# greater than equal to x will be moved to right
# less than x will be moved to left

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x):
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next

        ltail.next = right.next
        rtail.next = None

        return left.next

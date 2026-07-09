# Input  = 1 -> 2 -> 3 -> 4 -> 5 , left = 2,  right = 4
# Output = 1 -> 4 -> 3 -> 2 -> 5

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(next = head)
        leftPrev, curr = dummy, head

        for _ in range(left - 1):
            leftPrev = curr
            curr = curr.next

        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        leftPrev.next.next = curr
        leftPrev.next = prev

        return dummy.next
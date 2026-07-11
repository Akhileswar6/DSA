# Input  = 1 -> 2 -> 3 -> 4 -> 5,  k = 2
# Output = 1 -> 4 -> 3 -> 2 -> 5

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head, k):
        curr = head

        for _ in range(k - 1):
            curr = curr.next

        left = curr
        right= head

        while curr.next:
            curr = curr.next
            right = right.next

        left.val, right.val = right.val, left.val

        return head
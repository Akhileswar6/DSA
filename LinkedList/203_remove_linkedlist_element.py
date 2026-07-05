# Input  = 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6, val = 6
# Output = 1 -> 2 -> 3 -> 4 -> 5


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(next = head)
        prev, curr = dummy, head

        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr

        curr = nxt

        return dummy.next

        
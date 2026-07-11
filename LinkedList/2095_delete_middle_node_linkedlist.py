# Input  = 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6
# Output = 1 -> 3 -> 4 -> 1 -> 2 -> 6

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head):
        if not head.next:
            return None
        dummy = ListNode(next = head)
        slow, fast = dummy, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head
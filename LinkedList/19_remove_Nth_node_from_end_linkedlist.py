# Input  = 1 -> 2 -> 3 -> 4 -> 5,    n = 2
# Output = 1 -> 2 -> 3 -> 5

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(next = head)
        slow = fast = dummy

        for i in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next

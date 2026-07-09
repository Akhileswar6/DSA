# Input  = 1 -> 2 -> 3 -> 4 -> 5
# Output = 1 -> 3 -> 5 -> 2 -> 4

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        odd, even = head, head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return head

        
        
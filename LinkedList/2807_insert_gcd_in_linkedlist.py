# Input  = 18 -> 6 -> 10 -> 3
# Output = 18 -> 6 -> 6 -> 2 -> 10 -> 1 -> 3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head):
        curr = head

        while curr.next:
            g = gcd(curr.val , curr.next.val)

            new_node = ListNode(g)
            new_node.next = curr.next
            curr.next = new_node

            curr = new_node.next

        return head

# Input  =  4 -> 2 -> 1 -> 3
# Output =  1 -> 2 -> 3 -> 4


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        curr = head

        while curr:
            prev = dummy
            next_node = curr.next

            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            curr.next = prev.next
            prev.next = curr

            curr = next_node

        return dummy.next
        
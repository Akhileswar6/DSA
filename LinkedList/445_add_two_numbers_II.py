# Input  = l1 = 7 -> 2 -> 4 -> 3,  l2 = 5 -> 6 -> 4
# Output = 7 -> 8 -> 0 -> 7

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1)
            l1 = l1.next
        while l2:
            stack2.append(l2)
            l2 = l2.next

        carry = 0
        head = None

        while stack1 or stack2 or carry:
            total = carry

            total += stack1.pop() if stack1 else 0
            total += stack2.pop() if stack2 else 0

            carry = total // 10
            digit = total % 10

            node = ListNode(digit)

            node.next = head
            head = node

        return head



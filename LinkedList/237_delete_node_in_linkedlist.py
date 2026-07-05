# Input  = 4 -> 5 -> 1 -> 8     Node = 5
# Output = 4 -> 1 -> 9

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
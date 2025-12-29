class Node:
    def __init__(self, value: int, next: Node | None = None):
        self.val = value
        self.next = next


class Solution:
    def findMiddle(self, head: Node):
        s, f = head, head

        while f and f.next:
            s = s.next
            f = f.next.next

        return s

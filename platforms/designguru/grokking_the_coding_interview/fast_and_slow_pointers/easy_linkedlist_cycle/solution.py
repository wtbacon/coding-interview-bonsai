class Node:
    def __init__(self, value: int, next: Node | None = None):
        self.val = value
        self.next = next


class Solution:
    def hasCycle(self, head: Node):
        fast, slow = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

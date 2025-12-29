class Node:
    def __init__(self, value: int, next: Node | None = None):
        self.val = value
        self.next = next


class Solution:
    def findCycleStart(self, head: Node):
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        cur = slow
        length = 0
        while True:
            cur = cur.next
            length += 1

            if cur == slow:
                break

        p1, p2 = head, head
        while length > 0:
            p2 = p2.next
            length -= 1

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p2

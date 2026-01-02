class Node:
    def __init__(self, value: int, next: Node | None = None):
        self.val = value
        self.next = next


class Solution:
    def reorder(self, head: Node):
        if head.next is None or head.next.next is None:
            return head

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half_head = self._reverse(slow)
        first_half_head = head
        while first_half_head is not None and second_half_head is not None:
            tmp = first_half_head.next
            first_half_head.next = second_half_head
            first_half_head = tmp

            tmp = second_half_head.next
            second_half_head.next = first_half_head
            second_half_head = tmp

        # If the first_half_head node end at the slow node, a self-loop happens on the node.
        if first_half_head is not None:
            first_half_head.next = None

        return head

    def _reverse(self, head: Node) -> Node:
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev

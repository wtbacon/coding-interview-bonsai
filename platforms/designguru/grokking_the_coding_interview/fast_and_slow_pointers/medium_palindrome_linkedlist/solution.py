class Node:
    def __init__(self, value: int, next: Node | None = None):
        self.val = value
        self.next = next


class Solution:
    def isPalindrome(self, head: Node):
        if head.next is None:
            return True

        if head.next.next is None and head.val != head.next.val:
            return False

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reserved_second_half_head = self._reserve(slow)
        p1, p2 = head, reserved_second_half_head

        isPalindrome = True
        while p1 != slow:
            if p1.val != p2.val:
                isPalindrome = False
                break
            p1 = p1.next
            p2 = p2.next

        second_half_head = self._reserve(reserved_second_half_head)
        slow.next = second_half_head

        return isPalindrome

    def _reserve(self, head: Node) -> Node:
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev

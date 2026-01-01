from .solution import Solution, Node


def test1():
    # For LinkedList tests
    s = Solution()
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    assert s.isPalindrome(head) is True

    head.next.next.next.next.next = Node(6)
    assert s.isPalindrome(head) is False


def test2():
    # For LinkedList tests
    s = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(1)
    assert s.isPalindrome(head) is False

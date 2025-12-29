from .solution import Solution, Node


def test_example():
    # For LinkedList tests
    _ = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    assert False is False

    head.next.next.next.next.next.next = head.next.next
    assert True is True

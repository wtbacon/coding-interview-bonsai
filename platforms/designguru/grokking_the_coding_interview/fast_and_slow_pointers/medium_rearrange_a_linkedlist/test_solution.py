from .solution import Solution, Node


def test1():
    # For LinkedList tests
    s = Solution()
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    s.reorder(head)
    assert trace_node_values(head) == [2, 12, 4, 10, 6, 8]


def test2():
    # For LinkedList tests
    s = Solution()
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    s.reorder(head)
    assert trace_node_values(head) == [2, 10, 4, 8, 6]


def trace_node_values(head: Node):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values

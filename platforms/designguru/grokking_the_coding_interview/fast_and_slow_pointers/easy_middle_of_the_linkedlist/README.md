# Middle of the LinkedList

- Pattern: fast & slow pointers

## Problem

Given the head of a Singly LinkedList, return the middle node of it.
If the total number of nodes in it is even, return the second middle node.

## Notes

- Time: $O(N)$
- Space: $O(1)$
- Approach:
  1. Initialize both `slow` and `fast` pointers at the `head`.
  2. Iterate through the list
  3. When `fast` reaches the end of the list, `slow` will be positioned at the middle.
  4. If `fast.next` is None, it indicates the odd-length and return the middle node, or if `fast.next.next` is None, it indicates the even-length and return the second middle node.

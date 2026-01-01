# Palindrome LinkedList

- Pattern: Fast & Slow Pointers

## Problem

Given the head of a singly linked list, return `True` if the linked list is a palindrome, otherwise return `False`.

## Notes

- Time: $O(N)$
- Space: $O(1)$
- Approach:
  1. Use the fast & slow pointer technique to find the middle of the linked list.
  2. Reverse the second half of the linked list.
  3. Compare the first half and the reversed second half node by node.
  4. Restore the original linked list.
  5. Return `True` if all nodes matched, otherwise return `False`.

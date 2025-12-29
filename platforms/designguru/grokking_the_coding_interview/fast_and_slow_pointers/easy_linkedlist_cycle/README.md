# LinkedList Cycle

- Pattern: Fast & Slow Pointers

## Problem

Given the head of a singly LinkedList, return a boolean indicating whether the LinkedList contains a cycle.

## Notes

- Time: $O(N)$
- Space: $O(1)$
- Approach:
  1. Initialize two pointers(`slow` and `fast`) to point the head of the list.
  2. `slow` traverse the list by one step and `fast` by two steps in each iteration.
  3. If there is a cycle, the `fast` pointer will eventually lap the `slow` pointer.
  4. If the `fast` pointer reaches the end of the list, the list is acyclic.

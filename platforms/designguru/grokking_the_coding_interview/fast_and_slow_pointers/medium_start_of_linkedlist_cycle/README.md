# Start of LinkedList cycle (TODO: solve again)

- Pattern: fast & slow pointers

## Problem

Given the head of a Singly LinkedList that contains a cycle, return the starting node of the cycle.

## Notes

- Time: $O(N)$
- Space: $O(1)$
- Approach:
  1. Detect the cycle.
  2. Find the length of the LinkedList cycle.
  3. Initialize two pointers to point to the start of the LinkedList.
  4. Move one pointer ahead by the cycle length nodes.
  5. Keep incrementing two pointers until they both meet.
  6. Their meeting point is the starting node of the cycle.

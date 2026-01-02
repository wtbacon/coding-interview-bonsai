# Rearrange a LinkedList (TODO: Solve again)

- Pattern: Fast & Slow Pointers

## Problem

Given the head of a Singly LinkedList, return the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order.

## Notes

- Time: $O(N)$
  - Finding the middle of the LinkedList: $O(N)$ (to be precise, perform $N/2$ iterations)
  - Reversing the second half of the LinkedList: $O(N)$ (to be precise, perform $N/2$ iterations)
  - Merging the two halves: $O(N)$
- Space: $O(1)$
- Approach:
  1. Find the middle of the LinkedList using the fast & slow pointer technique.
  2. Reverse the second half of the LinkedList.
  3. Merge the two halves by alternately inserting nodes from the reversed second half into the first half.

# Cycle in a Circular Array (TODO: Solve again)

- Pattern: Fast & Slow Pointers

## Problem

We are given an array containing positive and negative numbers. Suppose the array contains a number `M` at a particular index. Now, if `M` is positive we will move forward `M` indices and if `M` is negative we will move backward `M` indices. You should assume that the array is circular which means two things:

1. If, while moving forward, we reach the end of the array, we will jump to the first index to continue the movement.
2. If, while moving backward, we reach the beginning of the array, we will jump to the last index to continue the movement.

Write a method to determine if the array has a cycle. The cycle is under the following restrictions:

- Should have more than one element
- Should follow one direction which means the cycle should not contain both forward and backward movements.

## Notes

- Time: $O(N^2)$
  - Iterate through each element takes $O(N)$ and perform a traversal takes $O(N)$.
- Space: $O(1)$
- Approach:
  1. Iterate through each element in the array.
  2. Find a cycle starting from that element using two pointers, a slow pointer and a fast pointer.
  3. While finding the cycle, the pointers should move in the same direction and should not encounter a single-element cycle.

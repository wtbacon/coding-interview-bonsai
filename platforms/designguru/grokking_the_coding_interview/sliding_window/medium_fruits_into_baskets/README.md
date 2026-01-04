# Fruits into Baskets

- Pattern: Sliding Window

## Problem

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an array `fruits`, where `fruits[i]` is the type of fruit the `i-th` tree produces.
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

1. You can only carry two baskets, and each basket can only hold one type of fruit.
2. You must pick exactly one fruit from every tree you visit.
3. You must start from any tree of your choice and move to the right. The picked fruits must fit in your baskets.

Return the maximum number of fruits you can pick.

## Notes

- Time: $O(N)$
- Space: $O(1)$
- Approach:
  1. Use a sliding window to keep track of the current window of fruits.
  2. Expand the window by moving the right pointer and adding fruits to the baskets.
  3. If the number of fruit types exceeds two, shrink the window from the left until we have at most two types of fruits.
  4. Keep track of the maximum window size during the process.

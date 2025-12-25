# Triplets with Smaller Sum

- Pattern: Two pointers

## Problem

Given an integer unsorted array `nums` and a target sum, return the number of triplets in it such that `arr[i] + arr[j] + arr[k] < target` where i, j, and k are three different indices.

## Notes

- Time: $O(N^2)$
  - Sort algorithm takes $O(N{log}N)$ and traversing the arr to search the triplets takes $O(N^2)$.
- Space: $O(1)$
- Approach: Sort the array first. Iterate through the array, using a two-pointer strategy for each element. If the current triplet sum is less than the target, it implies that all triplets formed with the current left pointer and any element between the left and right pointers will also satisfy the condition. Therefore, we can increment the count by `right - left`.

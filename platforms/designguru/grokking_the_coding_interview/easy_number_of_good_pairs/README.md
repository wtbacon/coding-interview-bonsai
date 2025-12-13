# Number of Good Pairs

- Pattern: HashMap

## Problem

Given an integer array `nums`, return the number of good pairs meet the requirements.
A pair $(i, j)$ is called good if $nums[i] = nums[j]$ and $i < j$.

## Notes

- Time: O(N)
- Space: O(N)
- Approach: Count the frequency of each number in the array and use the combination formula $_nC_{n-2} / 2$ for each frequency $n$ to calculate the total number of good pairs.

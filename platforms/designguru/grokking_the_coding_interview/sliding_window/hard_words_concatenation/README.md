# Words Concatenation

- Pattern: Sliding Window

## Problem

Given a string and a list of words, return all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

## Notes

- Time: $O(N * M * L)$
  - Where N = length of the string, M = number of words, L = length of each word.
- Space: $O(M + N)$
  - Where M = number of words, N = length of the string.
- Approach:
    - Use a sliding window approach to check every possible substring of the required length.
    - Maintain a frequency map of the words and compare it with the frequency of words found in the current window.
    - If they match, record the starting index.

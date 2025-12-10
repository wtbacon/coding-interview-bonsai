# Valid Anagram

- Pattern: HashMap

## Problem (write in your words)

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, otherwise return `False`.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

## Notes

- Time: O(n)
- Space: O(1)
- Approach: Use a hash map to count character frequencies, incrementing for characters in string `s` and decrementing for characters in string `t`.

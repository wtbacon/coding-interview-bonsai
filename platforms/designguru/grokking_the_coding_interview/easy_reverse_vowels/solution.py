class Solution:
    def reverseVowels(self, s: str) -> str:
        ls = list(s)
        vowels = "aeiouAEIOU"
        head, tail = 0, len(ls) - 1

        while head < tail:
            while head < tail and vowels.find(ls[head]) == -1:
                head += 1
            while head < tail and vowels.find(ls[tail]) == -1:
                tail -= 1
            ls[head], ls[tail] = ls[tail], ls[head]
            head += 1
            tail -= 1

        return "".join(ls)

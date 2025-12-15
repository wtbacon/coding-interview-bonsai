class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in freq_map:
                freq_map[s[i]] = 1
            else:
                freq_map[s[i]] += 1
            
            if t[i] not in freq_map:
                freq_map[t[i]] = -1
            else:
                freq_map[t[i]] -= 1
        
        for freq in freq_map.values():
            if freq != 0:
                return False

        return True

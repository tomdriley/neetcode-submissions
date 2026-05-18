class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorted_s = list(s)
        sorted_s.sort()
        sorted_t = list(t)
        sorted_t.sort()
        for i, _ in enumerate(sorted_s):
            if sorted_s[i] != sorted_t[i]:
                return False
        return True
        
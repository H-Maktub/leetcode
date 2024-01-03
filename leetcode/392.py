class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n = len(s)
        if n == 0:
            return True
        for ch in t:
            if s[i] == ch:
                i+=1
            if i == n:
                return True
        return False
class Solution:
    def scoreOfString(self, s: str) -> int:
        ret = 0
        for i in range(1,len(s)):
            ret += abs(ord(s[i-1])-ord(s[i]))
        return ret
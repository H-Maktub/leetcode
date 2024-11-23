from typing import List
class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        res = 0
        n = [0]*53
        p = [0]*53
        for i in range(26):
            n[i+1] = n[i]+nextCost[i]
            p[i+1] = p[i]+previousCost[i]
        for i in range(26):
            n[i+27] = n[i+26]+nextCost[i]
            p[i+27] = p[i+26]+previousCost[i]
        # print(n)
        # print(p)
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            cs = ord(s[i])-ord('a')
            ct = ord(t[i])-ord('a')
            a = 0
            if ct > cs:
                a += n[ct]-n[cs]
            else:
                a+= n[ct+26]-n[cs]
            b = 0
            if ct < cs:
                b += p[cs+1]-p[ct+1]
            else:
                b+= p[cs+27]-p[ct+1]
            # print(cs,ct,a,b)
            res += min(a,b)
        return res
a = Solution()
b = a.shiftDistance("a","b",[100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print(b)
b = a.shiftDistance("leet","code",[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
print(b)
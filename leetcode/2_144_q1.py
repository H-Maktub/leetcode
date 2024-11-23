class Solution:
    def canAliceWin(self, n: int) -> bool:
        res = False
        t = 10
        while n>0:
            n-=t
            t-=1
            if n < 0:
                return res
            res = not res
        return res

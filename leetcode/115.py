class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sl = len(s)
        tl = len(t)
        if sl<tl:
            return 0
        temp = [[0]*(tl+1) for _ in range(sl+1)]
        for i in range(sl+1):
            temp[i][tl] = 1
        for i in range(sl-1,-1,-1):
            for j in range(tl-1,-1,-1):
                if s[i] == t[j]:
                    temp[i][j] = temp[i+1][j+1]+temp[i+1][j]
                else:
                    temp[i][j] = temp[i+1][j]
        return temp[0][0]

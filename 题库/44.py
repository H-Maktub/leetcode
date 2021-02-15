class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        temp = [[False] * (m+1) for _ in range(n+1)]
        temp[0][0]= True
        for i in range(1,m+1):
            if p[i-1]=="*":
                temp[0][i] = True
            else:
                break

        for i in range(1,n+1):
            for j in range(1,m+1):
                if p[j-1] == "*":
                    temp[i][j] = temp[i][j-1] | temp[i-1][j]
                elif p[j-1] == "?" or s[i-1] == p[j-1]:
                    temp[i][j] = temp[i-1][j-1]

        return temp[-1][-1]
if __name__ == "__main__":
    a = Solution()
    b = a.isMatch("adceb","*a*b")
    print(b)
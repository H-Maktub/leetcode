##参考答案
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl, pl = len(s), len(p)
        def match(i,j)->bool:
            if i == 0:
                return False
            if p[j-1] == ".":
                return True
            return s[i-1] == p[j-1]
        temp =[[False] * (pl + 1) for _ in range(sl + 1)]
        temp[0][0] = True
        for i in range(sl+1):
            for j in range(1,pl+1):
                if p[j-1] == "*":
                    temp[i][j] |= temp[i][j-2]
                    if match(i,j-1):
                        temp[i][j] |= temp[i - 1][j]
                else:
                    if match(i, j):
                        temp[i][j] |= temp[i - 1][j - 1]
        return temp[sl][pl]

if __name__ == "__main__":
    a = Solution()
    b =a.isMatch("aabc",".*b.*")
    print(b)

from typing import Text
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        sl1 = len(s1)
        sl2 = len(s2)
        if sl1+sl2 != len(s3):
            return False
        temp = [[False] *(sl2+1) for _ in range(sl1+1)]
        temp[0][0]=True
        print(sl1,sl2,temp)
        for i in range(sl1+1):
            for j in range(sl2+1):
                t = i + j - 1
                if i>0:
                    print(i,j,t)
                    temp[i][j] = temp[i][j] or (temp[i-1][j] and s1[i-1] == s3[t])
                if j>0:
                    temp[i][j] = temp[i][j] or (temp[i][j-1] and s2[j-1] == s3[t])

        return temp[-1][-1]
if __name__ == "__main__":
    a = Solution()
    b = a.isInterleave("aabcc","dbbca","aadbbcbcac")
    print(b)
    b = a.isInterleave("a","","a")
    print(b)
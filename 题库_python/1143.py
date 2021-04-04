class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        temp = [[0]*(l2+1) for _ in range(l1+1)]
        print(temp)
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if text1[i-1] == text2[j-1]:
                    print(i,j,temp)
                    temp[i][j] = temp[i-1][j-1]+1
                else:
                    
                    temp[i][j] = max(temp[i-1][j],temp[i][j-1])
        return temp[-1][-1]

a = Solution()
b = a.longestCommonSubsequence("abcbdab","bdcaba")
print(b)
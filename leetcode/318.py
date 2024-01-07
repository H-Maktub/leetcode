from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        temp =[]
        for s in words:
            l = len(s)
            f = 0
            for ch in s:
                f |= 1<<(ord(ch)-ord('a'))
            temp.append([f,l])
        ans = 0
        for i in range(len(temp)):
            for j in range(i+1,len(temp)):
                if temp[i][0] & temp[j][0] == 0:
                    ans = max(ans,temp[i][1]*temp[j][1])
        return ans
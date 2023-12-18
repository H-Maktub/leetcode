from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        temp = {}
        ret = {}
        for i in range(len(s)-9):
            t = s[i:i+10]
            if t not in temp:
                temp[t] = 0
            elif t not in ret:
                ret[t] = 0
        return list(ret.keys())
    

a = Solution()
b = a.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print(b)
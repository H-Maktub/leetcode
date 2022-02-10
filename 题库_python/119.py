from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        ret = []
        for i in range(0,rowIndex):
            t = [1 for _ in range(0,i+1)]
            if len(t)>2:
                for j in range(1,i):
                    t[j] = ret[-1][j-1]+ret[-1][j]
            ret.append(t)
        return ret[-1]

a = Solution()
b = a.getRow(3)
print(b)
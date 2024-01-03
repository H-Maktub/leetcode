from curses.ascii import SO
from re import S
import re
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(0,numRows):
            t = [1 for _ in range(0,i+1)]
            if len(t)>2:
                for j in range(1,i):
                    t[j] = ret[-1][j-1]+ret[-1][j]
            ret.append(t)
        return ret

a = Solution()
b = a.generate(5)
print(b)
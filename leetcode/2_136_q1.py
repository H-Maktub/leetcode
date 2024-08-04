from typing import List,Counter
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        temp = [Counter() for _ in range(10)]
        for item in pick:
            temp[item[0]][item[1]] += 1
        res = 0
        for i in range(len(temp)):
            if len(temp[i].values())>0 and max(temp[i].values()) > i:
                res+=1
        return res
    

a = Solution()
b = a.winningPlayerCount(4,[[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]])
print(b)
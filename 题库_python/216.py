from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []

        def dfs(temp,start):
            if sum(temp) == n and len(temp) == k:
                ret.append(temp.copy())
                return
            for i in range(start,10):
                temp.append(i)
                dfs(temp,i+1)
                temp.pop()
        dfs([],1)
        return ret
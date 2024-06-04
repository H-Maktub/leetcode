from typing import List
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges)+1
        G = [[] for _ in range(n)]
        for u,v,w in edges:
            G[u].append((v,w))
            G[v].append((u,w))
        def dfs(p: int, root: int, curr: int) -> int:
            res = 0
            if curr == 0:
                res += 1
            for v, cost in G[p]:
                if v != root:
                    res += dfs(v, p, (curr + cost) % signalSpeed)
            return res
        res = [0]*n
        for i in range(n):
            pre = 0
            for v,cost in G[i]:
                cnt = dfs(v,i,cost % signalSpeed)
                res[i] += pre *cnt
                pre+=cnt
        return res
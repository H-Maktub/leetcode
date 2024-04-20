from typing import List
import heapq,math
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        temp = [[float("inf")] * (n + 1) for _ in range(n + 1)]
        temp[0][0] = 0
        for i in range(1,n+1):
            for j in range(i+1):
                if i != j:
                    temp[i][j] = min(temp[i][j],((temp[i-1][j] + dist[i-1]-1)//speed+1)*speed)
                if j != 0:
                    temp[i][j] = min(temp[i][j], temp[i-1][j-1]+dist[i-1])
        for j in range(n + 1):
            if temp[n][j] <= hoursBefore * speed:
                return j
        return -1

b = a.minSkips([1,3,2],4,2)
print(b)


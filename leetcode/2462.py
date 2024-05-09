from typing import List
import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l = -1
        r = len(costs)
        temp = []
        for i in range(candidates):
            l += 1
            r -= 1
            if l < r:
                heapq.heappush(temp,[costs[l],0])
                heapq.heappush(temp,[costs[r],1])
            elif l == r:
                heapq.heappush(temp,[costs[l],0])
        ret = 0
        for i in range(k):
            t = heapq.heappop(temp)
            ret += t[0]
            print(t,temp,l,r)
            if t[1] == 0 and l<r-1:
                l+=1
                heapq.heappush(temp,[costs[l],0])
            if t[1] == 1 and l<r-1:
                r-=1
                heapq.heappush(temp,[costs[r],1])
                
        return ret
    
a = Solution()
b = a.totalCost([17,12,10,2,7,2,11,20,8],3,4)
print(b)
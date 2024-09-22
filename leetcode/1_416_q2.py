from typing import List
import heapq
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        temp = []
        for i in range(len(workerTimes)):
            heapq.heappush(temp,[workerTimes[i],i,1])
        res = 0
        while mountainHeight > 0:
            top = heapq.heappop(temp)
            i = top[1]
            c = top[2]+1
            new = top[0]+workerTimes[i]*c
            heapq.heappush(temp,[new,top[1],c])
            mountainHeight -= 1
            res = max(res,top[0])
            # print(top[0],mountainHeight)
        return res
    

a = Solution()
b = a.minNumberOfSeconds(10,[3,2,2,4])
print(b)

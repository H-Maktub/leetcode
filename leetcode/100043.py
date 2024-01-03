from typing import List
import heapq
class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        temp = []
        heapq.heapify(temp)
        for i in range(0,len(values)):
            if len(values[i])>0:
                t = [values[i].pop(),i]
                heapq.heappush(temp,t)
        i = 1
        result = 0
        while temp:
            t = heapq.heappop(temp)
            result += t[0]*i
            i+=1
            if len(values[t[1]])>0:
                t = [values[t[1]].pop(),t[1]]
                heapq.heappush(temp,t)
            print(t,i)
            print(t[0]*i)
        return result
    
a = Solution()
b = a.maxSpending([[8,5,2],[6,4,1],[9,7,3]])
print(b)
            
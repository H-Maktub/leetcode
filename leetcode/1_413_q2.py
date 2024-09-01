from typing import List
import heapq
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        queries = [ abs(queries[i][0])+abs(queries[i][1]) for i in range(len(queries))]
        res = []
        temp = []
        for i in range(len(queries)):
            num = queries[i]
            if i < k-1:
                heapq.heappush(temp,-num)
                res.append(-1)
            elif i == k-1:
                heapq.heappush(temp,-num)
                res.append(-temp[0])
            else:
                if res[-1] > num:
                    heapq.heappop(temp)
                    heapq.heappush(temp,-num)
                res.append(-temp[0])
        return res
    
a = Solution()
b = a.resultsArray([[1,2],[3,4],[2,3],[-3,0]],2)
print(b)
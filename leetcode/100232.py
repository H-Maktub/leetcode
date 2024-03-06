from typing import List
import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        temp = []
        ret = 0
        for num in nums:
            if num < k:
                heapq.heappush(temp,num)
        while len(temp)>1:
            x = heapq.heappop(temp)
            y = heapq.heappop(temp)
            z = min(x,y)*2+max(x,y)
            if z < k:
                heapq.heappush(temp,z)
            ret+=1
        return ret+len(temp)

a = Solution()
b = a.minOperations([8,11,10,1,9],10)
print(b)
b = a.minOperations([1,1,2,4,9],20)
print(b)
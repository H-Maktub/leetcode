from typing import List
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        temp = []
        resut = []
        heapq.heapify(temp)
        for i in count:
            heapq.heappush(temp,[-count[i],i])
        for _ in range(k):
            a = heapq.heappop(temp)
            resut.append(a[1])
        return resut

a = Solution()
b = a.topKFrequent([1,1,1,2,2,3],2)
print(b)
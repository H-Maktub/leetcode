from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = []
        heapq.heapify(temp)
        for i in nums:
            heapq.heappush(temp,-i)
        for i in range(k-1):
            heapq.heappop(temp)
        return -heapq.heappop(temp)
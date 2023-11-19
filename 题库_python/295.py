from typing import List
import heapq
class MedianFinder:

    def __init__(self):
        self.count = 0
        self.lmin = []
        self.rmax = []

    def addNum(self, num: int) -> None:
        if self.count % 2 == 0:
            heapq.heappush(self.rmax,num)
            if self.count > 1:
                heapq.heappush(self.rmax,-heapq.heappop(self.lmin))
                heapq.heappush(self.lmin,-heapq.heappop(self.rmax))
        else:
            heapq.heappush(self.lmin,-heapq.heappushpop(self.rmax,num))
        self.count += 1

        

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (self.rmax[0]-self.lmin[0])/2
        else:
            return self.rmax[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
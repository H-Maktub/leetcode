from typing import Counter, List
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        temp = []
        result = []
        for i in range(0,len(nums)-k+1):
            print(i)
            if i == 0:
                temp = [[-nums[i],i] for i in range(k)]
                heapq.heapify(temp)
            else:
                heapq.heappush(temp,[-nums[i+k-1],i+k-1])
                while temp[0][1] < i:
                    heapq.heappop(temp)
                
            # print(temp)
            result.append(-temp[0][0])
        return result
1,3,-1,-3,5,3,6,7

a = Solution()
b = a.maxSlidingWindow([1,-1],1)
print(b)

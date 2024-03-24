from typing import List
import heapq
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        temp = {}
        tack = []
        ret = []
        for i in range(len(nums)):
            num = nums[i]
            count = freq[i]
            if num not in temp:
                temp[num] = 0
            temp[num] = max(0,count+temp[num])
            heapq.heappush(tack,[-temp[num],num])
            pre = None
            while True: 
                pre = heapq.heappop(tack)
                if temp[pre[1]] == - pre[0]:
                    heapq.heappush(tack,pre)
                    ret.append(temp[pre[1]])
                    break
        return ret
    

a = Solution()
b = a.mostFrequentIDs([2,3,2,1], [3,2,-3,1])
print(b)
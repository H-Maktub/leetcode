from typing import *
class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        temp = {}
        for i in range(len(nums)):
            if nums[i] in temp:
                temp[nums[i]][1] = i
            else:
                temp[nums[i]] = [i,i]
        li = sorted(temp.values(),key=lambda i:i[0])
        r = li[0][1]
        ret = 1
        for i in range(1,len(li)):
            if li[i][0] > r:
                ret=ret*2%(10**9+7)
            r = max(r,li[i][1])
        print(li)
        return ret
    
a = Solution()
b = a.numberOfGoodPartitions([1,2,1,3])
print(b)
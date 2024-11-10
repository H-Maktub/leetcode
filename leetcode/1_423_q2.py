from typing import List
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        temp = [1]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                temp[-1]+=1
            else:
                temp.append(1)
        # print(temp)
        res = max(temp)//2
        for i in range(1,len(temp)):
            res = max(res,min(temp[i-1],temp[i]))
        return res

a = Solution()
b = a.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1])
print(b)
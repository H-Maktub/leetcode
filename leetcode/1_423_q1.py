from typing import List
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        temp = [1]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                temp[-1]+=1
            else:
                temp.append(1)
        # print(temp)
        for t in temp:
            if t >= k*2:
                return True
        for i in range(1,len(temp)):
            if temp[i]>=k and temp[i-1]>=k:
                return True
        return False

a = Solution()
b = a.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1],3)
print(b)
b = a.hasIncreasingSubarrays([6,13,-17,-20,2],2)
print(b)
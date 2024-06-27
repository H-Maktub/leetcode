from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            if (nums[i]+ret)%2 == 0:
                ret+=1
                nums[i] = 1
        return ret
    
a = Solution()
b = a.minOperations([0,1,1,0,1])
print(b)

b = a.minOperations([1,0,0,0])
print(b)
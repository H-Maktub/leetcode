from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                ret+=1
                r = 0
                while r < 3:
                    if nums[i+r] == 0:
                        nums[i+r] = 1
                    else:
                        nums[i+r] = 0
                    r+=1
        if len(nums) != sum(nums):
            return -1
        return ret

    
a = Solution()
b = a.minOperations([0,1,1,1,0,0])
print(b)
b = a.minOperations([1,0,0,1,1])
print(b)
b = a.minOperations([1,0,0,1,1,0,1,1,1,0,0,0,1,0,1])
print(b)
        
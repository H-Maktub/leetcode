from typing import List
class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] | nums[j]) % 2 == 0:
                    return True
        return False
    

a = Solution()
b = a.hasTrailingZeros([2,4,8,16])
print(b)
b = a.hasTrailingZeros([1,3,5,7,9])
print(b)
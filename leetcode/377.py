from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        temp = [0] * (target+1)
        temp[0] = 1
        for i in range(1,target+1):
           for num in nums:
               if num <= i:
                   temp[i] += temp[i-num]
        return temp[-1]
    
a = Solution()
b = a.combinationSum4([1,2,3],4)
print(b)
b = a.combinationSum4([9],3)
print(b)
b = a.combinationSum4([4,2,1],32)
print(b)
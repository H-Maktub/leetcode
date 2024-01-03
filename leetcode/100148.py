from typing import List
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        ret = []
        for i in range(0,len(nums),2):
            # print(i)
            ret.append(nums[i+1])
            ret.append(nums[i])
        return ret
    
a = Solution()
b = a.numberGame([5,4,2,3])
print(b)
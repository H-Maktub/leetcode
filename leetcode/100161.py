from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        if len(nums) % 3 != 0:
            return []
        nums.sort()
        print(nums)
        ret = []
        for i in range(0,len(nums),3):
            if nums[i+1] - nums[i] <= k and nums[i+2] - nums[i+1] <= k and nums[i+2] - nums[i] <= k:
                ret.append([nums[i],nums[i+1],nums[i+2]])
            else:
                return []
        return ret
    


a = Solution()
b = a.divideArray([15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2],2)
print(b)
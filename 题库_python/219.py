from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = {}
        for i in range(len(nums)):
            if  nums[i] not in temp:
                temp[nums[i]] = i
            else:
                if i - temp[nums[i]] <=k:
                    return True
                else:
                    temp[nums[i]] = i
        return False
        

a = Solution()
b = a.containsNearbyDuplicate([1,2,3,1],3)
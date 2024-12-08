from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        temp = set(nums)
        if min(temp) < k:
            return -1
        if k in temp:
            return len(temp)-1
        return len(temp)
        

a = Solution()
b = a.minOperations([9,7,5,3],1)
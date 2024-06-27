from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            r = num // 3
            ret+=min(num%3,abs((r+1)*3-num))
        return ret
    

a = Solution()
b = a.minimumOperations([1,2,3,4])
print(b)
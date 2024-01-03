from typing import Counter, List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        temp = {0:1}
        pre = 0
        count = 0
        for num in nums:
            pre += num
            if pre-k in temp:
                count+=temp[pre-k]
            
            temp[pre] = temp.get(pre,0)+1
        return count

a = Solution()
b = a.subarraySum([1,-1,0],0)
print("============",b)
from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ret = 0
        for num in nums:
            ret^=num
        return f'{k^ret:b}'.count('1')


a = Solution()
b = a.minOperations([2,1,3,4],1)
print(b)
a = Solution()
b = a.minOperations([2,0,2,0],0)
print(b)

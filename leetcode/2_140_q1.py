from typing import List
class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = 10000
        for num in nums:
            t = 0
            while num != 0:
                t+=num%10
                num = num // 10
            res = min(res,t)
        return res
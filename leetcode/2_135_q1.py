from typing import List
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a = 0
        b = 0
        for num in nums:
            if num >= 10:
                b+=num
            else:
                a+=num
        if a==b:
            return False
        return True
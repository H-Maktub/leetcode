from typing import List, Text
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        tag = 1
        for num in nums:
            if num <0:
                tag = -tag
            elif num == 0:
                return 0
        return tag
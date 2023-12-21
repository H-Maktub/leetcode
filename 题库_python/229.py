from typing import List,Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = len(nums)/3
        n = Counter(nums)
        ret = []
        for i in n:
            if n[i] > t:
                ret.append(i)
        return ret
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        more = set()
        ret = set()
        for i in nums:
            if i in more:
                continue
            if i in ret:
                ret.remove(i)
                more.add(i)
            else:
                ret.add(i)
        return ret.pop()
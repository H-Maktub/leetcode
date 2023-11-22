from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ret = 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            ret = max(ret,min(i+1,citations[i]))
        return ret
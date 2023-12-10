from typing import List,Counter
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        ret = [0,0]
        for i in nums1:
            if i in n2:
                ret[0]+=1
        for i in nums2:
            if i in n1:
                ret[1]+=1
        return ret
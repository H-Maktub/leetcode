from collections import Counter
from typing import List
class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        
        self.dict1 = Counter(nums1)
        self.dict2 = Counter(nums2)
        self.nums1 = list(self.dict1)
        self.nums2 = nums2
        self.nums1.sort()
    def add(self, index: int, val: int) -> None:
        self.dict2[self.nums2[index]] -=1
        self.nums2[index] += val
        num = self.nums2[index]
        self.dict2[num]= self.dict2.get(num,0)+1

    def count(self, tot: int) -> int:
        t = 0
        
        for num in self.nums1:
            a = tot - num
            if a >= 0:
                t += self.dict1[num] * self.dict2.get(a,0)
            else:
                break
        return t



a = FindSumPairs([1,1,2,2,2,3],[1,4,5,2,5,4])
b = a.count(7)
print(b)
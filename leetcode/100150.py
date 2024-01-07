from typing import List
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)//2
        s1 = set(nums1)
        s2 = set(nums2)
        u = s1 & s2
        l1 = len(s1)
        l2 = len(s2)
        ul = len(u)
        print(s1,s2,u)
        if l1 > n:
            ul -= l1 -n
            l1 = n
        if l2 > n:
            ul -= l2 -n
            l2 = n

        print(l1,l2,ul)
        return l1+l2-max(0,ul)


a = Solution()
b = a.maximumSetSize([1,2,1,2], [1,1,1,1])
print(b)#2
b = a.maximumSetSize( [1,2,3,4,5,6],[2,3,2,3,2,3])
print(b)#5
b = a.maximumSetSize([1,1,2,2,3,3], [4,4,5,5,6,6])
print(b)#6
b = a.maximumSetSize([1,2,1,1],[1,2,3,4])
print(b)#4
b = a.maximumSetSize([1,1,1,1],[12,23,41,9])
print(b)#3
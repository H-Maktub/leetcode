from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        x = l//2
        y = l%2
        if y==0:
            return (nums1[x]+nums1[x-1])/2
        else:
            return nums1[x]

if __name__ == "__main__":
    a = Solution()
    b =a.findMedianSortedArrays([],[])
    print(b)
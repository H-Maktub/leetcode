from typing import List
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        def submin(nums1: List[int], nums2: List[int]) -> int:
            result = 0
            print(nums1,nums2)
            for i in range(len(nums1)):
                if nums1[i] > nums1[-1]:
                    nums1[i],nums2[i] = nums2[i],nums1[i]
                    print("===",i,nums1,nums2)
                    result+=1
                elif nums2[i] > nums2[-1]:
                    nums1[i],nums2[i] = nums2[i],nums1[i]
                    print("===",i,nums1,nums2)
                    result+=1
                if nums2[i] > nums2[-1] or nums1[i] > nums1[-1]:
                    print("=========")
                    result = -1
                    break
            return result
        l1 = submin(nums1.copy(),nums2.copy())
        nums1[-1],nums2[-1] = nums2[-1],nums1[-1]
        l2 = submin(nums1,nums2)
        if l1 == -1 and l2 == -1:
            return -1
        return min(l1,l2+1)
    
a = Solution()
b = a.minOperations([17,13,19,9,6,14],[17,14,15,1,19,19])
print(b)

b = a.minOperations([1,2,7],[4,5,3])
print(b)

b = a.minOperations([2,3,4,5,9],[8,8,4,4,4])
print(b)

b = a.minOperations([1,1,8,9],[1,7,1,1])
print(b)
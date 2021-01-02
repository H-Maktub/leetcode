from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i =0
        while i<n:
            nums1[m+i]=nums2[i]
            i +=1
        nums1.sort()  

if __name__ == "__main__":
    b = Solution()
    a = b.merge(nums1 = [1,2,0,0],m=2,nums2 = [1,2],n=2)#3
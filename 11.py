from typing import List
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         area = 0
#         length = len(height)
#         for i in range(length):
#             j = length-1
#             while j>i:
#                 area = max(area,min(height[i],height[j])*(j-i))
#                 if height[i]<height[j]:
#                     break
#                 j -= 1       
#         return area
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        i = 0
        j = len(height)-1
        while i<j:
            if height[i]>height[j]:
                area = max(area,height[j]*(j-i))
                j -=1
            else:
                area = max(area,height[i]*(j-i))
                i += 1
        return area


if __name__ == "__main__":
    a = Solution()
    b =a.maxArea([1,8,6,2,5,4,8,3,7])
    print(b)
   
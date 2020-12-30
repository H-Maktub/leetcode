from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        reslt = max(nums)
        for num in nums:
            if num >0:
                total = total + num
                reslt = max(reslt,total)
            elif total > 0:
                total = total + num
                if total < 0:
                    total = 0
                else:
                    reslt = max(reslt,total)  
        return reslt

if __name__ == "__main__":
    b = Solution()
    a = b.maxSubArray(nums = [1,2])#3
    a = b.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])#6
    a = b.maxSubArray(nums =[-1,-2])#-1
    a = b.maxSubArray(nums =[8,-19,5,-4,20])#21
    a = b.maxSubArray(nums =[1])#1
    a = b.maxSubArray(nums =[3,-2,-3,-3,1,3,0])#4
    a = b.maxSubArray(nums =[1,-3,2,0,-1,0,-2,-3,1,2,-3,2])#3
    a = b.maxSubArray(nums =[2,-3,1,3,-3,2,2,1])#6
    a = b.maxSubArray(nums =[-1,6,7,-7,-2,-6,-1,3,4,2,6,-3,-8,-1,7])#15
    a = b.maxSubArray(nums =[3,2,-2,1])#5

    # print ('aa',a)
    pass
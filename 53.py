from typing import List
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         result = nums[0]
#         all = nums[0]
#         a = 0
#         for i, num in enumerate(nums[1:]):
#             all = all+ num
#             print('all',num,all,result)
#             if all > result:
#                 result = all
#                 a = i+1
#             if num >= result:
#                 all = num
#                 result = num
#                 a = i+1
#                 temp = nums[a]
#                 maxSub = nums[a]
#                 x=a-1
#                 print('x',x)
#                 while x>=0:
#                     cache = temp + nums[x]
#                     maxSub = max(cache,maxSub)
#                     print('maxSub',nums,x,nums[x],cache,maxSub)
#                     temp = cache
#                     x=x-1
#                 print('----------',maxSub)
#                 result = maxSub

#         temp = nums[a]
#         maxSub = nums[a]
#         x=a-1
#         print('x',x)
#         while x>=0:
#             cache = temp + nums[x]
#             maxSub = max(cache,maxSub)
#             print('maxSub',nums,x,nums[x],cache,maxSub)
#             temp = cache
#             x=x-1
#             print('----------',maxSub)
#             result = maxSub
#         print('==========rest',result)
#         return result
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         result = 0
#         left = 0
#         right = len(nums)

#         while left<right and nums[left]<=0 :
#                 left = left+1
#         while left<right and nums[right-1]<=0 :
#                 right = right-1
#         result = max(result,self.totalList(nums[left:right]))
#         print(left,right,nums[left:right],self.totalList(nums[left:right]))
#         while right>left:
#             left = left+1
#             while left<right and nums[left]<=0 :
#                 left = left+1
#             result = max(result,self.totalList(nums[left:right]))
#             print('left',nums[left:right],self.totalList(nums[left:right]))
#             right = right-1
#             while left<right and nums[right-1]<=0 :
#                 right = right-1
#             result = max(result,self.totalList(nums[left:right]))
#             print('right',nums[left:right],self.totalList(nums[left:right]))
        
#         if result == 0:
#             result = nums[0]
#             for num in nums:
#                 result = max(num,result)
#         print('===============',result)
#         return result
#     def totalList(self,nums: List[int]) -> int:
#         total = 0
#         for num in nums:
#             total = total + num
#         return total
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        total = 0
        reslt = 0
        while left < len(nums):
            if nums[left] >0:
                total = total + nums[left]
            else:
                tmp = 0
                for num in nums[left:]:

                reslt = max(reslt,total)
                total = 0
            left = left+1
        reslt = max(reslt,total)
        print('--------------',reslt)
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
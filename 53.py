from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        all = nums[0]
        a = 0
        for i, num in enumerate(nums[1:]):
            all = all+ num
            print('all',num,all,result)
            if all > result:
                result = all
                a = i+1
            if num > result:
                all = num
                result = num
                a = i+1
       
        print(a,result)
        temp = nums[a]
        maxSub = nums[a]
        a=a-1
        while a>=0:
            cache = temp + nums[a]
            print('aaa',cache)
            maxSub = max(cache,maxSub)
            temp = cache
            a=a-1
        print('result',maxSub)
        return maxSub

if __name__ == "__main__":
    a = Solution.maxSubArray("",nums = [1,2])#3
    a = Solution.maxSubArray("",nums = [-2,1,-3,4,-1,2,1,-5,4])#6
    a = Solution.maxSubArray("",nums =[-1,-2])#-1
    a = Solution.maxSubArray("",nums =[8,-19,5,-4,20])#21
    a = Solution.maxSubArray("",nums =[1])#1
    a = Solution.maxSubArray("",nums =[3,-2,-3,-3,1,3,0])#3
    # print ('aa',a)
    pass
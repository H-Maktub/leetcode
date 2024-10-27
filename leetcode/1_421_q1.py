from typing import List
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def score(nums: List[int])-> int:
            m = min(nums)
            gcd = 1
            for i in range(1,m):
                ret = True
                for num in nums:
                    if num % (i+1) != 0:
                        ret = False
                        break
                if ret == True:
                    gcd = i+1
            lcm = nums[0]
            def maxCommonDivison(a,b):
                while(a*b != 0):
                    if(a > b):
                        a = a % b
                    elif(a < b):
                        b = b % a
                    else:
                        return a
                return max(a,b)
            for i in range(1,len(nums)):
                t = maxCommonDivison(lcm,nums[i])
                lcm = (lcm*nums[i])//t
            # print(gcd,lcm)
            return gcd * lcm
        res = score(nums)
        if len(nums) > 1:
            for i in range(len(nums)):
                res = max(res,score(nums[:i]+nums[i+1:]))
        return res
    
a = Solution()
# b = a.maxScore([2,4,8,16])
# print(b)
# b = a.maxScore([1,2,3,4,5])
# print(b)
b = a.maxScore([10,25,6])
print(b)
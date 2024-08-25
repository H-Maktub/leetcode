from typing import List,Counter
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def comp(a:int,b:int)->bool:
            a = str(a)
            b = str(b)
            n = max(len(a),len(b))
            if len(a) < n:
                a = "0"*(n-len(a))+a
            if len(b) < n:
                b = "0"*(n-len(b))+b
            c1 = ""
            c2 = ""
            c = 0
            for i in range(n-1,-1,-1):
                t1 = a[i]
                t2 = b[i]
                if t1 != t2:
                    c1+=t1
                    c2+=t2
                    c+=1 
                if c > 2:
                    break
            if c == 0:
                return True
            if c == 2:
                return c1 == c2[::-1]
            return False
        
        res = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if comp(nums[i],nums[j]):
                    res+=1
        return res
    
a = Solution()
# b = a.countPairs([3,12,30,17,21])
# print(b)
b = a.countPairs([490693,900498,448195,24359,126032,584252,26132,124479,586672,855404,24359,418495,243450,106232,690685,410981,871863,419180,242524,23549,284759,26132,271146,966337,781863,418495,242524,126032,411980,621032,271641,25349,900894,411980,997268,671059,649498,781836,312273,15727,671095])
print(b)
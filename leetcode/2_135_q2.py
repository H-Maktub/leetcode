import math
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        res = 0
        zmax = math.ceil(math.sqrt(r))
        zmin = math.floor(math.sqrt(l))
        for num in range(zmin,zmax+1):
            if num > 1:
                for i in range(2,int(num**0.5+1)):
                    if num % i == 0:
                        break
                else:
                    if num*num >= l and num*num<=r:
                        res+=1
        return r-l+1-res

a = Solution()
b = a.nonSpecialCount(1,4)
print(b)
b = a.nonSpecialCount(30594605,844702129)
print(b)
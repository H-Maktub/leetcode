from math import sqrt
class Solution:
    def countTriples(self, n: int) -> int:
        temp = 0
        max = n*n
        for i in range(1,n+1):
            for j in range(i,n+1):
                t = i*i+j*j
                if  t<=max and int(sqrt(t))==sqrt(t):
                    temp+=1
                    
        return temp*2

a = Solution()
b = a.countTriples(18)
print(b)
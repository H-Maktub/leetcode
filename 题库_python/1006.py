class Solution:
    def clumsy(self, N: int) -> int:
        ret = 0
        t = 1
        for i in range(N,0,-4):
            print("+++++",i)
            if i >3:
                ret += t* int(i*(i-1)/(i-2))+(i-3)
            elif i>2:
                ret += t* int(i*(i-1)/(i-2))
            elif i>1:
                ret += t* i*(i-1)
            else:
                ret += t*i
            t=-1
        
        return ret
            
a = Solution()
b = a.clumsy(1)
print(b)
b = a.clumsy(4)
print(b)
b = a.clumsy(5)

print(b)
b = a.clumsy(10)
print(b)
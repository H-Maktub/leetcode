class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        r1 = (n//2)*((m+1)//2)
        r2 = ((n+1)//2)*(m//2)
        print(r1,r2)
        return r1+r2
a = Solution()
b = a.flowerGame(3,2)
print(b)
b = a.flowerGame(1,1)
print(b)
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        i = 0
        for x in range(0,limit+1):
            for y in range(0,limit+1):
                for z in range(0,limit+1):
                    if x+y+z==n:
                        i+=1
        return i
    
a = Solution()
b = a.distributeCandies(5,2)
print(b)
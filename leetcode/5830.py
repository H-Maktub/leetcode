class Solution:
    def isThree(self, n: int) -> bool:
        temp = 0
        for i in range(2,n//2+1):
            print()
            if n%i == 0:
                temp+=1
        if temp == 1:
            return True
        return False



a = Solution()
b = a.isThree(12)
print(b)
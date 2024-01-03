class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        temp = [i+1 for i in range(n)]
        print(temp)
        ret = 0
        s = k-1
        while n>1:
            ret = temp.pop(s)
            n-=1
            s = (s+k-1)%n
        return temp[-1]
a = Solution()
b = a.findTheWinner(5,2)
print(b)
a = Solution()
b = a.findTheWinner(6,5)
print(b)

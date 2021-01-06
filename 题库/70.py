class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        l1=1
        l2=2
        a =0
        for i in range(3,n+1):
            a = l1+l2
            l1 = l2
            l2=a
        return a
if __name__ == "__main__":
    b = Solution()
    a = b.climbStairs(n=38)
    print(a)
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        i = 0
        l1min = max(0,n-2*limit)
        l1max = min(limit,n-l1min)
        # print("=====",l1min,l1max)
        for x in range(l1min,l1max+1):
            t = n-x
            l2max = max(min(limit,t),l1min)
            l2min = max(min(limit,t-l2max),l1min) 
            i+=l2max-l2min+1
            # print(x,l2max,l2min)
        return i 
a = Solution()
b = a.distributeCandies(5,2)
print(b)
b = a.distributeCandies(1,2)
print(b)
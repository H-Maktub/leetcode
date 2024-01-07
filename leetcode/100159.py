from functools import cache
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @cache
        def dfs(i,j)->int:
            if i == j:
                return 0
            if i < j:
                return j - i
            t1 = i % 11
            t2 = i % 5
            ret = i - j
            if ret == 1:
                return ret
            if ret > t1+1:
                ret = min(dfs((i-t1)//11,j)+t1+1,ret)
            if ret > 11-t1+1:
                ret = min(dfs((i-t1+11)//11,j)-t1+11+1,ret)
            if ret > t2+1:
                ret = min(dfs((i-t2)//5,j)+t2+1,ret)
            if ret > 5-t2+1:
                ret = min(dfs((i-t2+5)//5,j)-t2+5+1,ret)
            return ret
        return dfs(x,y)

# 3
# 4
# 5
# 1
# 2
# 16
a = Solution()
b = a.minimumOperationsToMakeEqual(26,1)
print(b)
b = a.minimumOperationsToMakeEqual(54,2)
print(b)
b = a.minimumOperationsToMakeEqual(25,30)
print(b)
b = a.minimumOperationsToMakeEqual(2,1)
print(b)
b = a.minimumOperationsToMakeEqual(5,3)
print(b)
b = a.minimumOperationsToMakeEqual(99,34)
print(b)
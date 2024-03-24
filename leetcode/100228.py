import math
class Solution:
    def minOperations(self, k: int) -> int:
        q = int(math.sqrt(k))
        if q == 1:
            return k-1
        a = k//q
        p = k % q
        if p == 0:
            return (q-1)+(a-1)
        ret = 0
        ret += p
        ret += q-p
        ret += a-1
        return ret
    
a = Solution()
b = a.minOperations(11)#5
print(b)
# b = a.minOperations(1)#0
# print(b)
# b = a.minOperations(2)#1
# print(b)
# b = a.minOperations(3)#2
# print(b)
# b = a.minOperations(4)#2
# print(b)
# b = a.minOperations(5)#3
# print(b)
# b = a.minOperations(6)#3
# print(b)

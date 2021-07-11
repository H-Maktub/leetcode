from typing import Counter
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        od = n // 2
        ev = n - od
        ans = pow(5, ev, 1000000007) * pow(4, od, 1000000007) % 1000000007
        return ans

a = Solution()
b = a.countGoodNumbers(1)
print("========",b)
b = a.countGoodNumbers(2)
print("========",b)
b = a.countGoodNumbers(4)
print("========",b)
b = a.countGoodNumbers(8)
print("========",b)
b = a.countGoodNumbers(16)
print("========",b)
b = a.countGoodNumbers(32)
print("========",b)
b = a.countGoodNumbers(64)
print("========",b)

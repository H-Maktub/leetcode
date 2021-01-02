import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))

if __name__ == "__main__":
    b = Solution()
    a = b.mySqrt(x=8)
    print(a)
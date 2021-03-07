from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)
if __name__ == "__main__":
    a = Solution()
    b = a.uniquePaths(3,3)
    print(b)

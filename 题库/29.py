class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = int(dividend/divisor)
        if a >2147483647:
            return 2147483647
        return a

if __name__ == "__main__":
    a = Solution()
    b = a.divide(7,-3)
    print(b)
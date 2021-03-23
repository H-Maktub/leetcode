class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            i = n %2
            n = n//2
            ret +=i
        return ret

if __name__ == "__main__":
    a = Solution()
    b = a.hammingWeight(11)
    print(b)
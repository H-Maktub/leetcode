class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

if __name__ == "__main__":
    b = Solution()
    a = b.addBinary(a="11",b="1")
    print(a)
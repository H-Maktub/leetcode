class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ""
        for i in range(len(s)//k):
            sub = s[i*k:i*k+k]
            total = 0
            for ch in sub:
                total+=ord(ch)-ord('a')
            total = total%26
            result+=chr(total+ord('a'))
        return result


a = Solution()
b = a.stringHash("abcd",2)
print(b)
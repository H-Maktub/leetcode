class Solution:
    def minChanges(self, n: int, k: int) -> int:
        i = 64
        ret = 0
        while i:
            a = n & 1
            b = k & 1
            if b == 1 and a != 1:
                ret = -1
                break
            if a != b:
                ret+=1
            i -=1
            n = n >> 1
            k = k >> 1
            
        return ret
a = Solution()
b = a.minChanges(13,4)
print(b)

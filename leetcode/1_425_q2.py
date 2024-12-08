from collections import defaultdict
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        temp = defaultdict(int)
        l = len(s)//k
        for i in range(k):
            temp[s[i*l:i*l+l]]+=1
        # print(temp)
        for i in range(k):
            ch = t[i*l:i*l+l]
            if temp[ch] <= 0:
                return False
            temp[ch]-=1
        return True
a = Solution()
b = a.isPossibleToRearrange("aabbcc","bbaacc",3)
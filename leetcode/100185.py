from typing import List,Counter
import collections
class Solution:
    def maximumLength(self, s: str) -> int:
        temp = collections.defaultdict(int)
        for i in range(len(s)):
            for j in range(i,len(s)):
                t = s[i:j+1]
                if len(Counter(t)) == 1:
                    temp[t]+=1
        ret = -1
        for k in temp:
            if temp[k]>=3:
                ret = max(ret,len(k))
        return ret
    

a = Solution()
b = a.maximumLength("abcdef")
print(b)
b = a.maximumLength("aaaa")
print(b)
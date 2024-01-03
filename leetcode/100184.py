from typing import List,Counter
import collections
class Solution:
    def maximumLength(self, s: str) -> int:
        ret = -1
        dep = ""
        temp = [collections.defaultdict(int) for _ in range(26)] 
        def count():
            nonlocal dep
            nonlocal temp
            nonlocal ret
            t = dep
            dep = ""
            l = len(t)
            if l <= ret:
                return
            key = ord(t[0])-ord('a')
            # print(temp,key)
            for i in range(l):
                temp[key][i+1]+=l-i
                if temp[key][i+1] >=3:
                    ret = max(ret,i+1)                
        for ch in s:
            if len(dep) == 0 or dep[-1] == ch:
                dep+=ch
            else:
                count()
                dep+=ch
        count()
        return ret
    

a = Solution()
b = a.maximumLength("abcdef")
print(b)
b = a.maximumLength("aaaa")
print(b)
b = a.maximumLength("abcaba")
print(b)
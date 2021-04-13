from typing import List
import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        temp = [str(i) for i in nums]
        def cmp(a, b):
            s1 = a+b
            s2 = b+a
            if s1>s2:
                return -1
            elif s1<s2:
                return 1
            return 0
        temp = sorted(temp, key=functools.cmp_to_key(cmp))
        ret = "0"
        for s in temp:
            if ret[0] == "0":
                ret = s
            else:
                ret+=s
        return ret
a = Solution()
b = a.largestNumber([3,30,34,5,9])
print(b)
b = a.largestNumber([0,0])
print(b)
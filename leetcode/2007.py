from typing import List
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 != 0:
            return []
        ret = []
        changed.sort()
        count = Counter(changed)
        for a in changed:
            if count[a] == 0:
                continue
            count[a] -= 1
            if count[a*2] == 0:
                return []
            count[a*2] -= 1
            ret.append(a)
        return ret

a = Solution()
b = a.findOriginalArray([1,3,4,2,6,8])
print(b)
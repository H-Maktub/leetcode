from typing import List
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        l = len(variables)
        ret = []
        for i in range(l):
            if i<l:
                v = variables[i]
                if (((v[0]**v[1])%10)**v[2])%v[3] == target:
                    ret.append(i)
        return ret


a = Solution()
b = a.getGoodIndices([[2,3,3,10],[3,3,3,1],[6,1,1,4]],2)
print(b)
from typing import List
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m = len(mat)
        n = len(mat[0])
        temp = set([0])
        for i in range(0,m):
            tt = set()
            for j in temp:
                for z in mat[i]:
                    if i == m-1:
                        a = abs(j+z-target)
                        if a == 0:
                            return 0
                        if a<=800:
                            tt.add(a)
                    else:
                        a = j+z
                        if a<=800:
                            tt.add(a)
            temp = tt
        return min(temp)

a = Solution()
b = a.minimizeTheDifference([[1,2,3],[4,5,6],[7,8,9]],13)
print("===========",b)
b = a.minimizeTheDifference([[1,2,9,8,7]],6)
print("===========",b)
b = a.minimizeTheDifference([[3,5],[5,10]],47)
print("===========",b)
b = a.minimizeTheDifference([[1]],1)
print("===========",b)
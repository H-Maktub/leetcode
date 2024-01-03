from os import rename
from typing import List
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        temp = []
        ret = 0
        for i in range(len(students)):
            s =students[i]
            temp.append([])
            for j in range(len(mentors)):
                m = mentors[j]
                ms = 0
                for z in range(len(s)):
                    if s[z] == m[z]:
                        ms+=1
                temp[i].append(ms)
        l = len(temp)
        def selsect(i,s,r):
            nonlocal ret
            if i == l:
                ret = max(ret,r)
            for j in range(l):
                if j not in s:
                    s.add(j)
                    selsect(i+1,s,r+temp[i][j])
                    s.remove(j)
        selsect(0,set(),0)
        return ret

# a = Solution()
# b = a.maxCompatibilitySum([[1,1,0],[1,0,1],[0,0,1]],[[1,0,0],[0,0,1],[1,1,0]])
# print("==============",b)

# a = Solution()
# b = a.maxCompatibilitySum([[0,0],[0,0],[0,0]], [[1,1],[1,1],[1,1]])
# print("==============",b)


a = Solution()
b = a.maxCompatibilitySum([[1,1,1],[0,0,1],[0,0,1],[0,1,0]],[[1,0,1],[0,1,1],[0,1,0],[1,1,0]])
print("==============",b)
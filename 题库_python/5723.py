from typing import List
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ret = [0]*k
        temp = {}
        for log in logs:
            i = log[0]
            t = log[1]
            if temp.get(i,None) == None:
                temp[i] = set()
            temp[i].add(t)
        for s in temp.values():
            t = len(s)
            if 0<t <=k:
                ret[t-1]+=1
        return ret

a = Solution()
b = a.findingUsersActiveMinutes([[0,5],[1,2],[0,2],[0,5],[1,3]],5)
print(b)
b = a.findingUsersActiveMinutes( [[1,1],[2,2],[2,3]],4)
print(b)
b = a.findingUsersActiveMinutes([[305589003,4136],[305589004,4139],[305589004,4141],[305589004,4137],[305589001,4139],[305589001,4139]],6)
print(b)
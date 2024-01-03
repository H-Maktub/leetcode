from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ret = [ -1 for _ in range(len(queries))]
        temp = {}
        for i in range(len(equations)):
            q = equations[i]
            if q[0] not in temp:
                temp[q[0]] = []
            temp[q[0]].append([q[1],values[i]]) 
            if q[1] not in temp:
                temp[q[1]] = []
            temp[q[1]].append([q[0],1/values[i]])
        # print(temp)
        runA = []
        def que(a,b,i,v):
            nonlocal runA
            nonlocal temp
            if a in temp:
                runA.append(a)
                l = temp[a]
                # print(l)
                for x in range(len(l)):
                    if l[x][0] not in runA:
                        if l[x][0] == b:
                            ret[i] = l[x][1]*v
                            break
                        else:
                            que(l[x][0],b,i,l[x][1]*v)

            
        for i in range(len(queries)):
            runA = []
            q = queries[i]
            if q[0] not in temp or q[1] not in temp:
                continue
            if q[0] != q[1]:
                que(q[0],q[1],i,1)
            else:
                ret[i] = 1
        return ret
            



a = Solution()
b = a.calcEquation([["a","b"],["b","c"],["bc","cd"]],[1.5,2.5,5.0],[["a","c"],["c","b"],["bc","cd"],["cd","bc"]])
print(b)
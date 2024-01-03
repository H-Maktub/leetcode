from typing import List
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        temp = collections.defaultdict(list)
        ind = [0]*numCourses
        result = []
        for v in prerequisites:
            temp[v[1]].append(v[0])
            ind[v[0]]+=1
        q = []
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
        while q:
            u = q.pop()
            result.append(u)
            for v in temp[u]:
                ind[v] -= 1
                if ind[v] == 0:
                    q.append(v)
        if len(result) != numCourses:
            return  []
        return result
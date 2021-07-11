from typing import List
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        temp = [0]*n
        for i in range(n):
            temp[i] = dist[i]//speed[i] + (0 if dist[i]%speed[i] == 0 else 1)
        print(temp)
        temp.sort()
        print(temp)
        for i in range(n):
            if i >= temp[i]:
                return i
        return n

a = Solution()
b = a.eliminateMaximum([1,3,4],[1,1,1])
print("=======",b)
b = a.eliminateMaximum([1,1,2,3],[1,1,1,1])
print("=======",b)
b = a.eliminateMaximum([3,5,7,4,5],[2,3,6,3,2])
print("=======",b)
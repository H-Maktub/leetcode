from typing import List
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        temp = {}
        for a in answers:
            a+=1
            if temp.get(a,None) == None:
                temp[a] = 0
            temp[a] +=1
        ret = 0
        for i,v in temp.items():
            ret+=v
            if v%i !=0:
                ret+=i-v%i
        return ret
a = Solution()
b = a.numRabbits([1, 1, 2])
print(b)
b = a.numRabbits([10, 10, 10])
print(b)
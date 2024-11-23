from typing import List
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        temp = [0]*(len(nums)+1)
        for q in queries:
            temp[q[0]]+=1
            temp[q[1]+1]-=1
        print(temp)
        for i in range(len(nums)):
            if temp[i] < nums[i]:
                return False
            temp[i+1]+=temp[i]
        return True
    
a = Solution()
# b = a.isZeroArray([1,0,1],[[0,2]])
# print(b)
# b = a.isZeroArray([4,3,2,1],[[1,3],[0,2]])
# print(b)
b = a.isZeroArray([1,8],[[1,1],[0,1],[1,1],[1,1],[1,1],[0,0],[0,0],[1,1],[1,1],[1,1],[0,0],[0,1],[1,1],[1,1],[1,1]])
print(b)
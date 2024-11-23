from typing import List
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        temp = [0]*(len(nums)+1)
        qs = len(queries)
        k = 0
        for i in range(len(nums)):
            while k < qs and temp[i] < nums[i]:
                q = queries[k]
                if i > q[1]:
                    k+=1
                    continue
                if i >= q[0] and i <= q[1]:
                    temp[i]+=q[2]
                else:
                    temp[q[0]]+=q[2]
                temp[q[1]+1]-=q[2]
                k+=1
                # print(k,temp)
            if temp[i] < nums[i]:
                return -1
            temp[i+1]+=temp[i]
        return k
a = Solution()
b = a.minZeroArray([0,10],[[0,1,2],[0,0,2],[0,1,2],[1,1,4],[0,1,3],[1,1,4],[0,1,2],[0,1,2],[0,1,2],[0,0,2],[1,1,2],[0,0,2],[0,0,3],[1,1,3],[0,0,5]])
print(b)
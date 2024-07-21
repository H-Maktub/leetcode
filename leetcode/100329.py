from typing import List
class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        temp = [ target[i] - nums[i] for i in range(len(nums))]
        ret = [ 0 for i in range(len(nums))]
        ret = temp[:]
        ret[0] = abs(temp[0])
        for i in range(1,len(temp)):
            if temp[i] > 0 and temp[i-1] > 0:
                if temp[i] > temp[i-1]:
                    ret[i] = min(ret[i],temp[i]-temp[i-1])
                else:
                    ret[i] = 0
            elif temp[i] < 0 and temp[i-1] < 0:
                if temp[i] < temp[i-1]:
                    ret[i] = min(-ret[i],abs(temp[i]-temp[i-1]))
                else:
                    ret[i] = 0
            else:
                ret[i] = abs(temp[i])
        # print(temp)
        # print(ret)
        return sum(ret)

a = Solution()
# b = a.minimumOperations([3,5,1,2],[4,6,2,4])
# print(b) #2
# b = a.minimumOperations([1,3,2],[2,1,4])
# print(b) #5
# b = a.minimumOperations([9,2,6,10,4,8,3,4,2,3],[9,5,5,1,7,9,8,7,6,5])
# print(b) # 20
b = a.minimumOperations([4,4,1,1,2,5,5,1,1],[3,2,3,4,5,2,3,3,4])
print(b) # 11
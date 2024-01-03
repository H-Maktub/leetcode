from typing import Counter, List
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        temp = Counter(nums)
        templist = list(temp.keys())
        templist.sort()
        result = 0
        for i in range(1,len(templist)):
            result += i*temp[templist[i]]
        return result

a = Solution()
b = a.reductionOperations([1,1,2,2,3])
print(b) 
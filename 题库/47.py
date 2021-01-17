from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        nums.sort()
        retList = []
        for i,num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue
            b = nums.copy()
            b.pop(i)
            tempList = self.permuteUnique(b)
            for temp in tempList:
                temp.insert(0,num)
                retList.append(temp)
        return retList

if __name__ == "__main__":
    a = Solution()
    b = a.permuteUnique([1,1,2])
    print('=====',b,len(b))
    b = a.permuteUnique([2,2,1,1])
    print('=====',b,len(b))
    # b = a.permute([5,4,6,2])
    # print('=====',b,len(b))
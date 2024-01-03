from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def combine(nums: List[int], k: int) -> List[List[int]]:
            retList = []
            if k==1:
                for i,val in enumerate(nums):
                    if i>0 and val == nums[i-1]:
                        continue     
                    retList.append([val])
                return retList

            for i,val in enumerate(nums):
                if i>0 and val == nums[i-1]:
                    continue     
                temp = combine(nums[i+1:],k-1)
                for a in temp:
                    retList.append(a+[val])
            return retList
        retList = []
        for i in range(len(nums)+1):
            temp = combine(nums,i)
            print(temp)
            retList.extend(temp)
        retList.append([])
        return retList

if __name__ == "__main__":
    a = Solution()
    b = a.subsetsWithDup([4,4,4,1,4])
    print("=====",b)
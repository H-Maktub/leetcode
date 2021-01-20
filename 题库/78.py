from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def combine(nums: List[int], k: int) -> List[List[int]]:
            retList = []
            if k==1:
                return [[i] for i in nums]
            for i,val in enumerate(nums):      
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
    b = a.subsets([1,2,3])
    print(b)
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = set(nums)
        nums.clear()
        nums.extend(list(a))
        nums.sort()
        return len(nums)
if __name__ == "__main__":
    nums= [-1,0,0,1,1,1,2,2,3,3,4]
    a = Solution.removeDuplicates("",nums=nums)
    print ('aa',a,nums)
    pass
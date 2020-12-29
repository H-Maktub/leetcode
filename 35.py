from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        for num in nums:
            if num >= target:
                break
            i = i+1 
        return i
    
if __name__ == "__main__":
    a = Solution.searchInsert("",nums = [1,3,5,6], target = 7)
    print ('aa',a)
    pass
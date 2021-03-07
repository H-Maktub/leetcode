from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i=0
        while i < n:
            if i>1 and nums[i]==nums[i-1]==nums[i-2]:
                nums.pop(i)
                n-=1
            else:
                i+=1
            
        return i

if __name__ == "__main__":
    a = Solution()
    b = a.removeDuplicates([1,1,1,2,2,3])
    print(b)
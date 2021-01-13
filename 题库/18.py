from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        numlist = []
        for i1 in range(n):
            if i1>0 and nums[i1]==nums[i1-1]:
                continue
            for i2 in range(i1+1,n):
                print(i2,i1>i1+1,nums[i2]==nums[i2-1])
                if i2>i1+1 and nums[i2]==nums[i2-1]:
                    print(i2)
                    continue
                tap = n-1
                for j in range(i2+1,n):
                    if j>i2+1 and nums[j]==nums[j-1]:
                        continue
                    while j<tap and nums[i1]+nums[i2]+nums[j]+nums[tap]>target:
                        tap -=1
                    if tap==j:
                        break
                    if nums[i1]+nums[i2]+nums[j]+nums[tap]==target:
                        print("============",nums[i1],nums[i2],nums[j],nums[tap])
                        numlist.append([nums[i1],nums[i2],nums[j],nums[tap]])
        return numlist

if __name__ == "__main__":
    a = Solution()
    b = a.fourSum([1, 0, -1, 0, -2, 2],0)
    print(b)
    b = a.fourSum([-2,-1,-1,1,1,2,2],0)
    print(b)

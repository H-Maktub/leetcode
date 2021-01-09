from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        numlist = []
        for i in range(n):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            tap = n-1
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                while j<tap and nums[i]+nums[j]>-nums[tap]:
                    tap -=1
                if tap==j:
                    break
                if nums[i]+nums[j]+nums[tap]==0:
                    print("============",nums[i],nums[j],nums[tap],j,tap)
                    numlist.append([nums[i],nums[j],nums[tap]])
        return numlist

if __name__ == "__main__":
    a = Solution()

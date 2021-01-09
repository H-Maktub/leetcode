from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        retnum = nums[0]+nums[1]+nums[2]

        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = n-1
            while left<right:
                num = nums[i]+nums[left]+nums[right]
                if abs(retnum -target)>abs(num-target):
                    retnum = num
                if num == target:
                    return num
                if num > target:
                    right -= 1
                else:
                    left +=1
                
        return retnum


if __name__ == "__main__":
    a = Solution()
    b = a.threeSumClosest([-1,2,1,-4],1)
    print(b)
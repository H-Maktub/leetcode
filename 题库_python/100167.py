from typing import List
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        r = n-1
        ret = 2
        for i in range(1,n):
            if nums[n-i] > nums[n-i-1]:
                r = n-i-1
            else:
                break
        print(r)
        for i in range(n-2):
            if i == 0 or nums[i-1] < nums[i]:
                r = max(r,i)
                print(r,n-r)
                ret+=n-r
            else:
                break
                
        return ret


a = Solution()

# b = a.incremovableSubarrayCount([6,5,7,8])
# print(b)

b = a.incremovableSubarrayCount([1,2,3,4])
print(b)
b = a.incremovableSubarrayCount([4,3,2,1])
print(b)

# b = a.incremovableSubarrayCount([8,7,6,6])
# print(b)

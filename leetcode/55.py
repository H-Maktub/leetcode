from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        n = len(nums)
        for i in range(n):
            if i<= jump:
                jump=max(jump,i+nums[i])
                if jump >= n-1:
                    return True
        return False

if __name__ == "__main__":
    a = Solution()
    b =a.canJump([2,3,1,1,4])
    print(b)
    b =a.canJump([3,2,1,0,4])
    print(b)
    b =a.canJump([2,5,0,0])
    print(b)
    b =a.canJump([3,0,8,2,0,0,1])
    print(b)
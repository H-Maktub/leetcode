from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            print(maxPos,i)
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                print("+++",maxPos,i,end)
                if i == end:
                    print("===",maxPos,i,end)
                    end = maxPos
                    step += 1
        return step

if __name__ == "__main__":
    a = Solution()
    b = a.jump([2,3,1,2,4,2,3])
    print("=======",b)
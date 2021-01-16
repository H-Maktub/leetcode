from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = -1
        j = -1
        try:
            i = nums.index(target)
            nums.reverse()
            j = len(nums)-1-nums.index(target)
        finally:
            return [i,j]

if __name__ == "__main__":
    a = Solution()
    b = a.searchRange([5,7,7,8,8,10],8)
    print(b)
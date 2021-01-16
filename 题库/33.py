from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = -1
        try:
            i = nums.index(target)
        finally:
            return i

if __name__ == "__main__":
    a = Solution()
    b = a.search([4,5,6,7,0,1,2],3)
    print(b)

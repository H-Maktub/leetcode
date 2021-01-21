from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        try:
            a = nums.index(target)
            return True
        except:
            return False

if __name__ == "__main__":
    a = Solution()
    b = a.search([2,5,6,0,0,1,2],0)
    print(b)
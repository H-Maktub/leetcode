from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        num = 1
        for i in nums:
            if num==i:
                num+=1
            elif num<i:
                break
        return num
if __name__ == "__main__":
    a = Solution()
    b = a.firstMissingPositive([1,2,0])
    print(b)
                

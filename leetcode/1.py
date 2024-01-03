from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        result = {}
        while i<len(nums):
            if nums[i] in result:
                return [result[nums[i]],i]
            result[target - nums[i]] = i
            i = i+1
        return None

if __name__ == "__main__":
    a = Solution.twoSum("",nums=[-1,-2,-3,-4,-5],target=-8)
    print(a)
    pass
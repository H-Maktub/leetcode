from typing import List
class NumArray:
    #
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.preNums = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.add(i+1,nums[i])

    def add(self,index:int, val:int):
        while index < len(self.preNums):
            self.preNums[index] += val
            index+= index & -index
    def preSum(self,index:int)->int:
        result = 0 
        while index:
            result += self.preNums[index]
            index -= index & -index
        return result

    def update(self, index: int, val: int) -> None:
        self.add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum(right + 1) - self.preSum(left)
from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.temp = [0]
        for num in nums:
            self.temp.append(self.temp[-1]+num)
    def sumRange(self, left: int, right: int) -> int:
        return self.temp[right+1]-self.temp[left]

if __name__ == "__main__":
    a = NumArray([-2,0,3,-5,2,-1])
    print(a.sumRange(0,2))
    


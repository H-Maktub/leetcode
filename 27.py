from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            try:
                nums.remove(val)
            except:
                break
        return len(nums)

if __name__ == "__main__":
    nums= [-1,0,0,1,1,1,2,2,3,3,4]
    a = Solution.removeElement("",nums=nums,val=2)
    print ('aa',a,nums)
    pass
from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        t = 0
        temp = set()
        for n in nums:
            n = int(n,2)
            temp.add(n)
        while t in temp:
            t+=1
        return bin(t)[2:].zfill(len(nums[0]))


a = Solution()
b = a.findDifferentBinaryString(["111","011","001"])
print("-------------",b)
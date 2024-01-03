from typing import List
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        t = []
        for i in nums:
            t.append(int(i))
        t.sort(reverse=True)
        return str(t[k-1])


a = Solution()
b = a.kthLargestNumber( ["2","21","12","1"],3)
print(b)
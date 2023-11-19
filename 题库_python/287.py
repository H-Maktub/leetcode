class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = {}
        for num in nums:
            if num not in temp:
                temp[num] = 0
            else:
                return num
        return -1
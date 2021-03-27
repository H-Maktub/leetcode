class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        left = [float("inf") for _ in range(n)]
        for i in range(1,n):
            left[i] = min(left[i-1],nums[i-1])
        temp = []
        for i in range(n-1,-1,-1):
            t = float("-inf")
            while temp and temp[-1]<nums[i]:
                t = temp.pop()

            if left[i]<t:
                return True
            
            temp.append(nums[i])
        return False
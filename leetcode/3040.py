class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(l,r,target):
            if l >= r:
                return 0
            ret = 0
            if nums[l]+nums[l+1] == target:
                ret = max(ret,1+dfs(l+2,r,target))
            if nums[r]+nums[r-1] == target:
                ret = max(ret,1+dfs(l,r-2,target))
            if nums[l]+nums[r] == target:
                ret = max(ret,1+dfs(l+1,r-1,target))
            return ret
        
        ret = 0
        ret = max(ret, dfs(0, n - 1, nums[0] + nums[1]))
        ret = max(ret, dfs(0, n - 1, nums[0] + nums[n - 1]))
        ret = max(ret, dfs(0, n - 1, nums[n - 2] + nums[n - 1]))
        return ret
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = [0] * len(grid[0])
        for g in grid:
            for i in range(len(g)):
                ans[i] = max(ans[i],len(str(g[i])))
        return ans
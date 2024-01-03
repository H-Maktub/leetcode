from typing import List
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        to_answer = [[] for _ in range(n)]

        ans = [0] * len(queries)
        for i, (u, v) in enumerate(queries):
            if u > v: u, v = v, u
            if u == v or heights[u] < heights[v]: ans[i] = v
            else: to_answer[v].append((i, heights[u]))
        print("======1",to_answer,ans)
        stack = [(-1, float("inf"))]
        for idx in range(n-1, -1, -1):
            while stack[-1][1] <= heights[idx]:
                print("+++++++",stack)
                stack.pop()
            
            for i, v in to_answer[idx]:
                l, r = 0, len(stack) - 1
                print("--------",idx,v,l,r,stack)
                while l <= r:
                    m = (l + r) // 2
                    if stack[m][1] > v: l = m + 1
                    else: r = m - 1
                ans[i] = stack[r][0]
                print(">>>>>>>>>",ans,i)
            stack.append((idx, heights[idx]))
            print(stack,ans)
        return ans
a = Solution()
b = a.leftmostBuildingQueries([6,4,8,5,2,7],[[0,1],[0,3],[2,4],[3,4],[2,2]])
print(b)
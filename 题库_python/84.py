from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        ret = 0
        temp = [-1]
        for i in range(n):
            while heights[temp[-1]] > heights[i]:
                h = heights[temp.pop()]
                w = i-temp[-1]-1
                ret = max(ret,h*w)
            temp.append(i)
        return ret


if __name__ == "__main__":
    a = Solution()
    b = a.largestRectangleArea([2,1,5,6,2,3]) #10
    print(b)
from typing import List
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        temp = []
        ret = 0
        colors += colors[0:k-1]
        for color in colors:
            if len(temp) == 0 or temp[-1] == color:
                temp = [color]
                continue
            if temp[-1] != color:
                temp.append(color)
            if len(temp) >= k:
                ret+=1
        return ret
    
a = Solution()
b = a.numberOfAlternatingGroups([0,1,0,1,0],k=3)
print(b)
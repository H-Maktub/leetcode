from typing import List
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        temp = []
        ret = 0
        colors += colors[0:2]
        for color in colors:
            if len(temp) == 0 or temp[-1] == color:
                temp = [color]
                continue
            if temp[-1] != color:
                temp.append(color)
            if len(temp) >= 3:
                ret+=1
        return ret

a = Solution()
b = a.numberOfAlternatingGroups([0,1,0,0,1])
print(b)
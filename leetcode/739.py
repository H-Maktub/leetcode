from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(temp) > 0 and temp[-1][1] < temperatures[i]:
                t = temp.pop()
                result[t[0]] = i - t[0]
                
                    
            temp.append([i,temperatures[i]])
        return result
    
a = Solution()
b = a.dailyTemperatures([73,74,75,71,69,72,76,73])
print(b)

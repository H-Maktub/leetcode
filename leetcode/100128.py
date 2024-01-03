
from typing import List
class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        result = []
        temp = {}
        for t in access_times:
            name = t[0]
            time = int(t[1])
            if name not in temp:
                temp[name] = []
            temp[name].append(time)
            
        for name,time in temp.items():
            time.sort()
            if len(time)>=3:
                for i in range(0,len(time)-2):
                    if time[i+2]//100 - time[i]//100 == 0 or (time[i+2]//100 - time[i]//100 == 1 and time[i+2]%100 - time[i]%100 < 0):
                        print(time[i+2],time[i],time[i+2]/100 - time[i]/100)
                        result.append(name)
                        break
        return result
a = Solution()
b = a.findHighAccessEmployees([["akuhmu","0454"],["aywtqh","0000"],["akuhmu","0518"],["ihhkc","0439"],["ihhkc","0508"],["akuhmu","0529"],["aywtqh","0000"],["aywtqh","0001"]])
print(b)

b = a.findHighAccessEmployees([["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]])
print(b)




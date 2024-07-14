from typing import List
class Solution:
    def validStrings(self, n: int) -> List[str]:
        temp = ["0","1"]
        for i in range(1,n):
            new = []
            for s in temp:
                if s[-1] == "0":
                    new.append(s+"1")
                else:
                    new.append(s+"0")
                    new.append(s+"1")
            temp = new
        return temp

a = Solution()
b = a.validStrings(3)
print(b)
        
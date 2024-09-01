class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        n1 = str(num1)
        n2 = str(num2)
        n3 = str(num3)
        n1 = "0"*(4-len(n1))+n1
        n2 = "0"*(4-len(n2))+n2
        n3 = "0"*(4-len(n3))+n3
        res = ""
        for i in range(4):
            res+=str(min(n1[i],n2[i],n3[i]))
        return int(res)
class Solution:
    def isBalanced(self, num: str) -> bool:
        a = 0
        b = 0
        for i in range(len(num)):
            if i % 2 == 0:
                a+=int(num[i])
            else:
                b+=int(num[i])
        return a==b
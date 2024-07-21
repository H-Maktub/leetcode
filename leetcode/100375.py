class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        ret = "Bob"
        while x > 0 and y > 3:
            x-=1
            y-=4
            if ret == "Bob":
                ret = "Alice"
            else:
                ret = "Bob"
        return ret
    

a = Solution()
b = a.losingPlayer(4,11)
print(b)
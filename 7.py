class Solution:
    def reverse(self, x: int) -> int:
        r = True

        if x < 0 :
            r = False
            x = -x
        s = str(x)
        s = s[::-1]
        if int(s)> 2147483648:
            return 0
        return int(s) if r else -int(s)

if __name__ == "__main__":
    a = Solution.reverse("",x=1534236469)
    print ('aa',a)
    pass
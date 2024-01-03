class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            # 抹去最右边的 1
            right = right & (right - 1)
        return right

    
a = Solution()
b = a.rangeBitwiseAnd(5,7)
print(b)
b = a.rangeBitwiseAnd(0,0)
print(b)
b = a.rangeBitwiseAnd(1,2147483647)
print(b)
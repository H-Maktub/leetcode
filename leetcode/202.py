class Solution:
    def isHappy(self, n: int) -> bool:
        temp = []
        while n != 1 and n not in temp:
            temp.append(n)
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            n = total_sum
        return n == 1
    

a = Solution()
b = a.isHappy(2)
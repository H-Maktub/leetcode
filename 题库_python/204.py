class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        temp = [1] * n
        temp[0] = temp[1] = 0
        for i in range(2,int(n**0.5)+1):
            if temp[i] == 1:
                print(i,temp[i*i:n:i])
                temp[i*i:n:i] = [0] * ((n - 1 - i * i) // i + 1)
        return sum(temp)
    

a = Solution()
b = a.countPrimes(100)
print(b)
temp = [i for i in range(100)]
print(temp[3:1])
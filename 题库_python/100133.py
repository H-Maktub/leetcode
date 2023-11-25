from typing import List
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        if len(prices) <= 2:
            return prices[0]
        temp = [[0,0] for _ in range(len(prices))]
        temp[0] = [prices[0],prices[0]]
        temp[1] = [prices[0],prices[0]+prices[1]]
        for i in range(2,len(prices)):
            temp[i][1] = min(temp[i-1][0],temp[i-1][1])+prices[i]
            temp[i][0] = temp[i][1]
            t = i
            while t > i-t:
                
                z = temp[t-1][1]
                print(t,i,z)
                temp[i][0] = min(temp[i][0],z)
                t-=1
        print(temp)
        return min(temp[-1])

a = Solution()
b = a.minimumCoins([3,1,2])
print(b)
print("=========")
b = a.minimumCoins( [1,10,1,1])
print(b)


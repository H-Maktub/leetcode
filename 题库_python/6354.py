class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        result = 0
        result += min(k,numOnes)
        k -= min(k,numOnes)
        print(k,result)
        k -= min(k,numZeros)
        print(k,result)
        result += -min(k,numOnes)
        k -= min(k,numOnes)
        return result
    
a = Solution()
b = a.kItemsWithMaximumSum(3,2,0,4)
print(b)
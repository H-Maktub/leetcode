from typing import List
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        k1 = k
        k2 = len(reward1) - k
        temp = [[reward1[i],reward2[i],reward1[i]-reward2[i]] for i in range(len(reward1))]
        print(temp)
        result = 0
        temp.sort(key=lambda x:x[2])
        for i in range(min(k1,len(temp))):
            result += temp.pop()[0]
            k1 -= 1
        temp.sort(key=lambda x:x[2],reverse=True)
        for i in range(min(k2,len(temp))):
            result += temp.pop()[1]
            k2 -= 1
        return result
    
a = Solution()
b = a.miceAndCheese([1,1,3,4],[4,4,1,1],2)
print(b)
b = a.miceAndCheese([1,4,4,6,4],[6,5,3,6,1],1)
print(b)
b = a.miceAndCheese([4,1,5,3,3],[3,4,4,5,2],3)
print(b)
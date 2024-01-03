from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        temp = [0]
        for i in range(1,num+1):
            temp.append(temp[i>>1]+(i&1))
        return temp
if __name__ == "__main__":
     a= Solution()
     print(a.countBits(5))

#0000
#0001
#0010
#0011
#0100
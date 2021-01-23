class Solution:
    def numTrees(self, n: int) -> int:
        retList = [1]
        for i in range(1,n):
            temp = 0
            for x in range(i+1):
                if x ==0 or x== i:
                    temp+=retList[i-1]
                else:
                    
                    left = retList[x-1]
                    right = retList[i-x-1]
                    print("=====",left,right)
                    temp+=left*right
                    pass
            retList.append(temp)
        print(retList)
        return retList[-1]


if __name__ == "__main__":
    a = Solution()
    b = a.numTrees(4)
    print(b)
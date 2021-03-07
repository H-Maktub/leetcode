from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        retList = []
        i = 0
        while i<n:
            print("++++",i,n-i-1)
            left = self.generateParenthesis(i)
            right = self.generateParenthesis(n-i-1)
            print("====",i,left,n-i-1,right)
            lefttemp = []
            if len(left)>0:
                for leftstr in left:
                    lefttemp.append("("+leftstr+")")
            else:
                lefttemp.append("()")

            print("lefttemp",lefttemp)
            
            if len(right)>0:
                for temp in lefttemp:
                    for rightStr in right:
                        retList.append(temp+rightStr) 
            else:
                retList.extend(lefttemp)

            
            i +=1
        return retList

if __name__ == "__main__":
    a = Solution()
    b = a.generateParenthesis(3)
    print(b)
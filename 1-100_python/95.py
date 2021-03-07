from typing import List, Mapping
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def getTrees(start:int, end:int) -> List[TreeNode]:
            if start == end:
                return [TreeNode(start)]
            retList =[]
            for i in range(start,end+1):
                if i == start:
                    rightList = getTrees(i+1,end)
                    for tree in rightList:
                        temp = TreeNode(i)
                        temp.right = tree
                        retList.append(temp)
                elif i==end:
                    leftList = getTrees(start,i-1)
                    for tree in leftList:
                        temp = TreeNode(i)
                        temp.left = tree
                        retList.append(temp)
                else:
                    leftList = getTrees(start,i-1)
                    rightList = getTrees(i+1,end)
                    for left in leftList:
                        for right in rightList:
                            temp = TreeNode(i)
                            temp.left = left
                            temp.right = right
                            retList.append(temp)
                
            return retList
                    
        return getTrees(1,n)


if __name__ == "__main__":
    a = Solution()
    b = a.generateTrees(4)
    print(len(b))
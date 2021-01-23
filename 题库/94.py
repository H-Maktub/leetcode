from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def found(temp: TreeNode)-> List[int]:
            if temp == None:
                return []
            retList = []
            if temp.left != None:
                retList.extend(found(temp.left))
            retList.append(temp.val)
            if temp.right != None:
                retList.extend(found(temp.right))
            return retList
        return found(root)
import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValid(temp:TreeNode,x:int,y:int)->bool:
            if temp==None:
                return True
            if not (x<temp.val<y):
                return False
            left = isValid(temp.left,x,temp.val)
            right = isValid(temp.right,temp.val,y)
            return left and right
        left = isValid(root.left,-sys.maxsize,root.val)
        right = isValid(root.right,root.val,sys.maxsize)
        return left and right

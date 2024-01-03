from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def  jisum(root,targgetSum):

            if root is None:
                return 0
            
            ret = 0
            if  root.val == targgetSum:
                ret += 1
            ret += jisum(root.left,targgetSum - root.val)
            ret += jisum(root.right,targgetSum - root.val)
            return ret
        
        if root is None:
            return 0
        ret = jisum(root,targetSum)
        ret += self.pathSum(root.left,targetSum)
        ret += self.pathSum(root.right,targetSum)
        return ret
a = Solution()
b = a.pathSum(TreeNode(5,TreeNode(4),TreeNode(3)),9)
print(b)



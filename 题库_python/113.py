from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []
        def dfs(root:TreeNode,targetSum:int,pathSum:List[int]):
            pathSum.append(root.val)
            t = targetSum - root.val
            if t == 0 and root.left == None and root.right == None:
                ret.append(pathSum)
            else:
                if root.left:
                    dfs(root=root.left,targetSum=t,pathSum=pathSum[:])
                if root.right:
                    dfs(root=root.right,targetSum=t,pathSum=pathSum[:])
        if root:
            dfs(root=root,targetSum=targetSum,pathSum=[])
        return ret

a = Solution()
b = a.pathSum(TreeNode(val=1),1)
print("===============",b)
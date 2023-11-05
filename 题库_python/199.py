from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def dfs(root,depth):
            nonlocal ret
            if root is None:
                return
            if len(ret) == depth:
                ret.append(root.val)
            else:
                ret[depth] = root.val
            dfs(root.left,depth+1)
            dfs(root.right,depth+1)
        dfs(root,0)
        return ret
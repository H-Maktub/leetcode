from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            dfs(root.right)
            ret.append(root.val)
        dfs(root)
        return ret
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ret:'TreeNode' = None
        def dfs(root,p,q)->bool:
            nonlocal ret
            if root is None:
                return False
            l = dfs(root.left,p,q)
            r = dfs(root.right,p,q)
            if (l and r) or ((root == p or root == q) and (l or r)):
                ret = root
            return l or r or root == p or root == q
        
        dfs(root,p,q)
        return ret
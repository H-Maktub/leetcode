class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(l:TreeNode,r:TreeNode):
            if l==None and r == None:
                return True
            if l==None or r==None:
                return False
            return l.val==r.val and dfs(l.right,r.left) and dfs(l.left,r.right)
        return dfs(root,root)
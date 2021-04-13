class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        ret = float('inf')
        t = -1
        def dfs(root):
            nonlocal t
            nonlocal ret
            if root == None:
                return
            dfs(root.left)
            if t==-1:
                t = root.val
            else:
                ret = min(ret,root.val-t)
                t = root.val    
            dfs(root.right)
        dfs(root)
        return ret

a = Solution()
b = a.minDiffInBST(root=TreeNode(val=90,left=TreeNode(val=69,left=TreeNode(val=49),right=TreeNode(val=89))))
print(b)
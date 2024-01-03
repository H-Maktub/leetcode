class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def dfs(t):
            nonlocal ret
            if t != None:
                ret+=1
                dfs(t.left)
                dfs(t.right)
        dfs(root)
        return ret
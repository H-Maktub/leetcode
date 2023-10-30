from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1
        def dp(t:TreeNode):
            nonlocal ans
            if t == None:
                return 0
            l = dp(t.left)
            r = dp(t.right)
            ans = max(ans,l+r+1)
            return max(l,r)+1
        dp(root)
        return ans - 1

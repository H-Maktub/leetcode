from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if root is None:
                return []
            ret = []
            ret += dfs(root.left)
            ret.append(root.val)
            ret += dfs(root.right)
            return ret
        ret = dfs(root)
        return ret[k-1]
a = Solution()
b = a.kthSmallest(TreeNode(3),1)
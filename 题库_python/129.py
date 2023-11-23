from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def dfs(t:TreeNode,val):
            nonlocal ret
            if t.left != None:
                dfs(t.left,val*10+t.val)
            if t.right != None:
                dfs(t.right,val*10+t.val)
            if t.left == t.right == None:
                ret+=val*10+t.val
                print(val*10+t.val)
        if root != None:
            dfs(root,0)
        return ret
a = Solution()
b = a.sumNumbers(TreeNode(1,TreeNode(2),TreeNode(3)))
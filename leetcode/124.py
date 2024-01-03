from re import S
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = root.val
        def subMax(p:TreeNode)->int:
            nonlocal ret
            if p == None:
                return 0
            left = max(subMax(p.left),0)
            right = max(subMax(p.right),0)
            sum = p.val + left+right
            ret = max(ret,sum)
            return max(left,right)+p.val
        subMax(root)
        return ret

a = Solution()
b = a.maxPathSum(TreeNode(-10,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7))))
print(b)
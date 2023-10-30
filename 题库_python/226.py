# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        p = root
        def sw(t:TreeNode):
            if t != None:
                t.left,t.right = t.right,t.left
                sw(t.left)
                sw(t.right)
        sw(p)
        return root
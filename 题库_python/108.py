import builtins
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(l,r):
            if l>r:
                return None
            pass
    
        return build(0,len(nums)-1)
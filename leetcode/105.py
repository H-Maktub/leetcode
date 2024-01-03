from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildtree(pre_l,pre_r,in_l,in_r):
            if pre_l>pre_r:
                return None
            pre_root = pre_l
            in_root = index[preorder[pre_root]]
            root = TreeNode(preorder[pre_root])
            size_l  = in_root-in_l
            root.left = buildtree(pre_l+1,pre_l+size_l,in_l,in_root-1)
            root.right = buildtree(pre_l+size_l+1,pre_r,in_root+1,in_r)
            return root
        n = len(preorder)
        index = {v:i for i,v in enumerate(inorder)}
        return buildtree(0,n-1,0,n-1)

a = Solution()
b = a.buildTree([3,9,20,15,7],[9,3,15,20,7])
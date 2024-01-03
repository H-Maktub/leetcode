from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(in_l,in_r):
            if in_l>in_r:
                return None
            value = postorder.pop()
            in_root = index[value]
            root = TreeNode(value)
            root.right = build(in_root+1,in_r)
            root.left = build(in_l,in_root-1)
            return root

        n = len(inorder)
        index = {v:i for i,v in enumerate(inorder)}
        return build(0,n-1)

a = Solution()
b = a.buildTree([9,3,15,20,7],[9,15,7,20,3])
print(b)
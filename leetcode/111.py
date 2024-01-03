class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        result = float('inf')
        def depue(root,d):
            nonlocal result
            if root.left == None and root.right == None:
                if result<d+1:
                    return result
                result = min(result,d+1)
            if root.left:
                depue(root.left,d+1)
            if root.right:
                depue(root.right,d+1)
        if not root:
            return 0
        depue(root,0)
        return result
a = Solution()
b= a.minDepth(None)
print(b)
        
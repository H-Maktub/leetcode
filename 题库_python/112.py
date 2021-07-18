class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None and root.val == targetSum:
            return True
        elif root.left != None and self.hasPathSum(root.left,targetSum-root.val):
            return True
        elif root.right != None and self.hasPathSum(root.right,targetSum-root.val):
            return True
        return False


a = Solution()
b = a.hasPathSum(None,1)
print("===============",b)
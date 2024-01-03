class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root == None:
            return
        temp = root
        while temp.left or temp.right:
            if temp.left:
                tr = temp.right
                temp.right = temp.left
                tl = temp.left
                temp.left = None
                while tl.right:
                    tl = tl.right
                else:
                    tl.right = tr
            temp = temp.right
a = Solution()
root = TreeNode(1,TreeNode(2,TreeNode(3,),TreeNode(4,)),TreeNode(5,None,TreeNode(6)))
a.flatten(root)
while root:
    print("====",root.val)
    root = root.right
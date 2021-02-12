class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        x,y,z = None, None, None
        temp=[]
        while temp or root:
            while root:
                temp.append(root)
                root = root.left
            root = temp.pop()
            if z and root.val<z.val:
                y = root
                if x==None:
                    x = z
                else:
                    break
            z = root
            root = root.right
        t = x.val
        x.val = y.val
        y.val = t
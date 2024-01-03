class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.temp =[]
        self.dp(root)
    def dp(self,root):
        while root:
            self.temp.append(root)
            root = root.left

    def next(self) -> int:
        t = self.temp.pop()
        self.dp(t.right)
        return t.val

    def hasNext(self) -> bool:
        return bool(self.temp)
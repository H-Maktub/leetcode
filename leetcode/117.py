
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        temp = [root]
        while len(temp) != 0:
            for i in range(1,len(temp)):
                temp[i-1].next = temp[i]
                temp[i].next = None
            t = []
            for i in temp:
                if i.left:
                    t.append(i.left)
                if i.right:
                    t.append(i.right)
            temp = t    
        return root
from curses import noecho
from os import nice
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        temp = [root]
        while len(temp) != 0:
            for i in range(1,len(temp)):
                temp[i-1].next = temp[i]
                temp[i].next = None
            t = []
            if temp[0].left != None:
                for i in temp:
                    t.append(i.left)
                    t.append(i.right)
            temp = t    
        return root
from typing import Optional
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        temp = {}
        def copy(n:Node):
            nonlocal temp
            if n.val not in temp:
                t = Node(n.val)
                temp[n.val] = t
                if n.neighbors != None:
                    for nn in n.neighbors:
                        copy(nn)
                        t.neighbors.append(temp[nn.val])
        if node != None:
            copy(node)           
            return temp[node.val]
        return None


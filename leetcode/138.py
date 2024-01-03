
# Definition for a Node.
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        dict = {}
        old = head
        while(old):
            if dict.get(old) == None:
                dict[old] = Node(old.val)
            if old.next != None:
                if dict.get(old.next) == None:
                    dict[old.next] = Node(old.next.val)
                dict[old].next = dict[old.next]
            if old.random != None:
                if dict.get(old.random) == None:
                    dict[old.random] = Node(old.random.val)
                dict[old].random = dict[old.random]
            old = old.next
        return dict[head]
    
a = Solution()
b = a.copyRandomList(Node(1,next=Node(2)))
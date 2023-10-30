from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        ll = []
        while (head):
            ll.append(head)
            head = head.next
        ll.sort(key=lambda node: node.val)
        for i in range(1,len(ll)):
            ll[i-1].next = ll[i]
            ll[i].next = None
        return ll[0]
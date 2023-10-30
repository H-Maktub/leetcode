from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa = headA
        pb = headB
        while(pa != pb):
            pa = pa.next if pa != None else headB
            pb = pb.next if pb != None else headA
        return pa
# Definition for singly-linked list.
from typing import List,Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        while cur != None:
            if cur.next != None and cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        if head != None and head.val == val:
            return head.next
        return head



a = Solution()
b = a.removeElements(ListNode(7,ListNode(7,ListNode(7))),7)

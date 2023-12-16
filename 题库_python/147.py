from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while head:
            temp.append(head)
            head = head.next
        temp.sort(key=lambda p:p.val)
        for i in range(len(temp)-1):
            temp[i].next = temp[i+1]
            temp[i+1].next = None
        return temp[0]

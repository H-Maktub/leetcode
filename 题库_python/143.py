from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = []
        t = head
        while t:
            temp.append(t)
            t = t.next
        x=0
        y = len(temp)-1
        while x <= y:
            if x != y:
                temp[x].next = temp[y]
            temp[y].next = None
            if x > 0:
                temp[y+1].next = temp[x]
            x+=1
            y-=1
        return head
    


a = Solution()
b = a.reorderList(ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))
while b:
    print(b.val)
    b = b.next
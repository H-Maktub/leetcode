from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        a = head
        b = a.next
        c = b
        while a and b:
            if b != None:
                a.next= b.next
                if a.next != None:
                    a = a.next
            if a != None:
                b.next = a.next
                b = b.next
        a.next = c
        return head
    
a = Solution()
b = a.oddEvenList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))))
while b:
    print(b.val)
    b = b.next
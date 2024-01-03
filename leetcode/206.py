from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        next = head.next
        head.next = None
        i = 0
        while(next and i<10):
            i += 1
            b = head
            while(b):
                print(b.val)
                b = b.next
            print("=======",head.val,next.val)
            temp = next.next
            next.next = head
            head = next
            next = temp

        return head

a = Solution()
b = a.reverseList(ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))
while(b):
    print(b.val)
    b = b.next
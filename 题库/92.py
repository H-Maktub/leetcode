from typing import Literal


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        temp = []
        x = 1
        while head:

            temp.append(head)
            head = head.next
            if x == n:
                break
            x+=1
        temp[m-1].next = temp[n-1].next
        for i in range(m,n):
            print(temp[i].val)
            temp[i].next = temp[i-1]
        if m==1:
            return temp[-1]
        else:
            temp[m-2].next = temp[-1]
            return temp[0]
            

if __name__ == "__main__":
    a = Solution()
    b = a.reverseBetween(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))),3,4)
    while b:
        print("====",b.val)
        b = b.next
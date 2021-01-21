from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ret = None
        temp = None
        tempSet = set()
        while head:
            if head.next and head.val == head.next.val:
                tempSet.add(head.val)         
            if head.val not in tempSet:
                if ret == None:
                    ret = head
                    temp = head
                else:
                    temp.next = head  
                    temp = head
            head = head.next
        if temp:
            temp.next = None
        return ret

if __name__ == "__main__":
    a = Solution()
    b = a.deleteDuplicates(ListNode(1,ListNode(2,ListNode(2))))
    while b:
        print(b.val)
        b = b.next
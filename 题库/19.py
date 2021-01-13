# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp = head
        listheader = []
        while tmp:
            listheader.append(tmp)
            tmp = tmp.next
        lenght = len(listheader)
        n =lenght-n
        if n == 0:
            if lenght==1:
                return None
            else:
                print('=====================')
                head = listheader[0].next
        elif n==lenght -1:
            print('=====================+')
            listheader[n-1].next=None
        else:
            print('=======================----')
            listheader[n-1].next = listheader[n+1]
        return head


if __name__ == "__main__":
    a = Solution()
    b = a.removeNthFromEnd(ListNode(1,ListNode(2)),2)
    print(b)
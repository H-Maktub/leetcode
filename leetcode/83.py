class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dupSet=set()
        a = head
        tmp = a
        while a != None:
            print(a.val)
            if a.val in dupSet:
                tmp.next = a.next
                a = tmp
            else:
                tmp = a
                dupSet.add(a.val)
            a = a.next
        return head


if __name__ == "__main__":
    l1 = ListNode(x=1)
    l1.next=ListNode(x=1)
    b = Solution()
    a = b.deleteDuplicates(head=l1)
    print(a)
    while a != None:
        print("RESLUT",a.val)
        a = a.next
    pass
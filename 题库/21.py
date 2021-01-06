class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        ret = result
        while l1 and l2:
            if l1.val < l2.val:
                result.next = l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next
            result = result.next
        else:
            if l2 != None:
                result.next = l2
            else:
                result.next = l1
        return ret.next
if __name__ == "__main__":
    l1 = ListNode(val=1,next=ListNode(val=2,next=ListNode(val=4)))
    l2 = ListNode(val=1,next=ListNode(val=3,next=ListNode(val=4)))
    a = Solution.mergeTwoLists("",l1=l1,l2=l2)
    print(a)
    while a != None:
        print("RESLUT",a.val)
        a = a.next
    pass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = l1
        tag = None
        up  = 0
        while l1 != None and l2 != None:
            l = l1.val+ l2.val + up
            if l> 9:
                l = l-10
                up = 1
            else:
                up = 0
            l1.val = l
            tag =l1
            l1 = l1.next
            l2 = l2.next
        else:
            if l2 != None:
                tag.next = l2
                l1 = l2
        while up > 0 and l1 != None:
            l = l1.val + up
            if l> 9:
                l = l-10
                up = 1
            else:
                up = 0
            l1.val = l
            tag = l1
            l1 = l1.next
        if up >0:
            tag.next = ListNode(val=up)
        return result
        

if __name__ == "__main__":
    # l1 = ListNode(val=9)
    # l2 = ListNode(val=9)
    # l2 = ListNode(val=9,next=ListNode(val=9,next=ListNode(val=9,next=ListNode(val=9))))
    # l1 = ListNode(val=9)
    l1 = ListNode(val=3)
    l2 = ListNode(val=7,next=ListNode(val=3))

    a = Solution.addTwoNumbers("",l1=l1,l2=l2)
    while a != None:
        print("RESLUT",a.val)
        a = a.next
    while l1 != None:
        print("l1",l1.val)
        l1 = l1.next
    while l2 != None:
        print("l2",l2.val)
        l2 = l2.next
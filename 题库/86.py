class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left = None
        tleft = None
        right = None
        tright = None
        while head:
            if head.val < x:
                if left == None:
                    left=head
                    tleft = head
                else:
                    left.next = head
                    left = head
            else:
                if right == None:
                    right = head
                    tright = head
                else:
                    right.next = head
                    right = head

            head = head.next

        if right:
            right.next = None
        if tleft == None:
            return tright
        else:
            left.next = tright
            return tleft
            

if __name__ == "__main__":
    a = Solution()
    b = a.partition(ListNode(1,ListNode(4,ListNode(3,ListNode(2,ListNode(5,ListNode(2)))))),3)
    while b:
        print(b.val)
        b = b.next
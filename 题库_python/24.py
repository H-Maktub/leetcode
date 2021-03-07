class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head ==None:
            return head
        elif head.next == None:
            return head
        tmp = head.next
        left = None 
        while head != None:
            temp = head.next
            if temp != None:
                head.next = temp.next
                temp.next = head
            else:
                break
            if left != None:
                left.next = temp
            left = head
            head = head.next      
        return tmp

if __name__ == "__main__":
    a = Solution()
    b = a.swapPairs(ListNode(1,ListNode(2,ListNode(3))))
    while b:
        print(b.val)
        b = b.next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(temp):
            for i in range(1,k):
                temp[k-i].next = temp[k-i-1]
            
        temp= []
        i = 1
        ret = None
        left = None
        while head:
            temp.append(head)
            if i==k:
                head = head.next
                if ret == None:
                    ret = temp[-1]
                    left = temp[0]
                else:
                    left.next = temp[-1]
                    left = temp[0]
                reverse(temp)
                temp.clear()
                i=1
            else:
                i+=1
                head = head.next
        else:
            if ret == None:
                return head
            else:
                for i in temp:
                    left.next = i
                    left = i
            left.next = None
        return ret


if __name__ == "__main__":
    a = Solution()
    b = a.reverseKGroup(ListNode(1,ListNode(2,)),2)
    while b:
        print(b.val)
        b = b.next
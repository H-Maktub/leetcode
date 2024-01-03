class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k ==0 or  head == None or head.next == None:
            return head
        temp =[]
        top = head
        while top:
            temp.append(top)
            if top.next ==None:
                top.next = head
                break
            else:
                top = top.next
        k = k%len(temp)
        temp[-k-1].next=None
        return temp[-k]

if __name__ == "__main__":
    a = Solution()
    b = a.rotateRight(None,0)
    while b:
        print(b.val)
        b=b.next
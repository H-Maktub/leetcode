from typing import List, Text
import functools
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        temp = []
        for i in lists:
            while i:
                temp.append(i.val)
                i = i.next
        print(temp)
        temp.sort()
        n = len(temp)
        if n == 0:
            return None
        temp[0] = ListNode(temp[0])
        for i in range(1,n):
            temp[i] = ListNode(temp[i])
            temp[i-1].next=temp[i]
        temp[n-1].next = None
        return temp[0]


if __name__ == "__main__":
    a = Solution()
    b = a.mergeKLists([ListNode(1,ListNode(4,ListNode(5))),ListNode(1,ListNode(3,ListNode(4))),ListNode(2,ListNode(6))])
    print(b)
    while b:
        print(b.val)
        b = b.next

    def numeric_compare(x, y):
        return x - y

    print(sorted([5, 2, 4, 1, 3], key=lambda x:x))
# Definition for singly-linked list.
from typing import List,Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        while head:
            if head.val in nums:
                 head = head.next
                 continue
            break
        ret = head
        while head:
            if head.next != None and head.next.val in nums:
                head.next = head.next.next
            else:
                head = head.next
        return ret
    


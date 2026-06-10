# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr:
            next = curr.next
        prev = None
        while curr:
            curr.next = prev
            prev = curr
            curr = next
            if next:
                next = curr.next
        return prev
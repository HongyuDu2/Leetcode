# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        pre = dummy
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            pre.next = b
            a.next = b.next
            b.next = a
            pre = a
        return dummy.next
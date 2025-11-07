# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
    self, l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
            dummy = ListNode(0)
            cur = dummy
            p, q = l1, l2
            while p and q:
                if p.val <= q.val:
                    cur.next = p
                    p = p.next
                else:
                    cur.next = q
                    q = q.next
                cur = cur.next
            cur.next = p if p else q
            return dummy.next
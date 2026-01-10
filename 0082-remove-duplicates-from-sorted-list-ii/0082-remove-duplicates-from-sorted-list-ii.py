# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head

        while cur:
            if cur.next and cur.val == cur.next.val:
                duplicate_val = cur.val
                while cur and cur.val == duplicate_val:
                    cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        
        return dummy.next
                
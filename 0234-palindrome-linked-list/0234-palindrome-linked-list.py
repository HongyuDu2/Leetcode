# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        second = prev

        p1, p2 = head, second
        ok = True
        while p2:
            if p1.val != p2.val:
                ok = False
                break
            p1, p2 = p1.next, p2.next
        
        return ok

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head and not head.next:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        second = pre
        p1, p2 = head, second
        ok = True
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

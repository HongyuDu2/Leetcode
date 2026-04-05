# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPre = dummy

        def getk(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        while True:
            kth = getk(groupPre, k)
            if not kth:
                break
            groupNext = kth.next

            cur, pre = groupPre.next, kth.next
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            
            tmp = groupPre.next
            groupPre.next = kth
            groupPre = tmp
        
        return dummy.next



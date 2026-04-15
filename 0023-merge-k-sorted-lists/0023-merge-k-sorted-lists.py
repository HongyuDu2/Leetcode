# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        
        # 第一步：把所有节点的值取出来
        for node in lists:
            while node:
                vals.append(node.val)
                node = node.next
        
        # 第二步：排序
        vals.sort()
        
        # 第三步：重建链表
        dummy = ListNode(0)
        cur = dummy
        for val in vals:
            cur.next = ListNode(val)
            cur = cur.next
        
        return dummy.next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res: List[int] = []
        def depth(node, length):
            if not node:
                return
            if length == len(res):
                res.append(node.val)
            depth(node.right, length + 1)
            depth(node.left, length + 1)
        depth(root, 0)
        return res
        
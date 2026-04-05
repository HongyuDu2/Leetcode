# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def dfs(node, current, path):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                if node.val == current:
                    res.append(path[:])
            dfs(node.left, current-node.val, path)
            dfs(node.right, current-node.val, path)
            path.pop()
        dfs(root, targetSum, [])
        return res
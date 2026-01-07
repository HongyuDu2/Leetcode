# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build(l, r):
            if l > r:
                return [None]
            
            res = []
            for root_val  in range(l, r+1):
                left_trees = build(l, root_val-1)
                right_trees = build(root_val+1, r)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        return build(1,n)



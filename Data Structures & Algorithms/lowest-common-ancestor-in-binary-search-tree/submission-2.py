# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lowestCommonAncestor = root
        if p.val > q.val:
            p, q = q, p

        while True:
            if (root.val > p.val) and (root.val < q.val):
                return lowestCommonAncestor
            
            if (root.val == p.val) or (root.val == q.val):
                return root

            
            elif root.val > q.val :
                root = root.left
            
            elif root.val < q.val:
                root = root.right

            lowestCommonAncestor = root

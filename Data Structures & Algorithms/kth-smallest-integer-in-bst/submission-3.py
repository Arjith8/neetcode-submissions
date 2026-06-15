# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = 0
        resp = 0
        def dfs(node):
            nonlocal current
            nonlocal resp
            if not node:  
                return current
            
            dfs(node.left)
            current += 1
            if current == k:
                resp = node.val
            dfs(node.right)
            
        dfs(root)
        return resp
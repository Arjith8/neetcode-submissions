# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        resp = [root.val]
        max_dept = 0
        def dfs(node, height):
            nonlocal max_dept
            if not node:
                return
            
            if height > max_dept:
                resp.append(node.val)
                max_dept += 1
            
            dfs(node.right, height + 1)
            dfs(node.left, height + 1)
        
        dfs(root, 0)
        return resp
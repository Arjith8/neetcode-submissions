# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # the smallest will be the left most node in the bst
        # 2nd smallest will be the parent of that node 
        # 3rd smallest will be the right node 

        stack = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            stack.append(node)
            dfs(node.right)
        
        dfs(root)
        return stack[k - 1].val
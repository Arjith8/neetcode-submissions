# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 1
        stack = [(root.left, root.val), (root.right, root.val)]
        while stack:
            current, prev_val = stack.pop()
            if not current:
                continue
            
            if current.val >= prev_val:
                count += 1
            
            stack.extend([
                (current.left, max(current.val, prev_val)),
                (current.right, max(current.val, prev_val))
            ])

        return count
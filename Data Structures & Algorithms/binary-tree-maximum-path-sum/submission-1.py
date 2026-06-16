# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        response = root.val
        def traverse(node, current_best):
            nonlocal response
            if not node:
                return 0
            left_side_best = node.val + traverse(node.left, current_best)
            right_side_best = node.val + traverse(node.right, current_best)
            current_best = max(node.val, left_side_best, right_side_best)

            response = max(response, current_best, right_side_best + left_side_best - node.val)

            return current_best
        
        traverse(root, float("-infinity"))
        return response

        
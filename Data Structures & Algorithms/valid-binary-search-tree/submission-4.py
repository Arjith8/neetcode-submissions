# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, left, right):
            # print(root.val, left, right)
            if not root:
                return True
            if root.val <= left or root.val >= right:
                return False

            return check(root.left, left, root.val) and check(root.right, root.val, right)

        return check(root, float("-infinity"), float("infinity"))
        
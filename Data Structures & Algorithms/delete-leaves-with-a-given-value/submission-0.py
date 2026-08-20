# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        def dfs(node):
            if node is None: return False
            delete_node = dfs(node.left)
            if delete_node:
                node.left = None

            delete_node = dfs(node.right)
            if delete_node:
                node.right = None

            if node.val == target and node.left is None and node.right is None:
                return True
            return False
        dfs(root)
        if root.val == target and root.left is None and root.right is None:
            return None
        return root
        
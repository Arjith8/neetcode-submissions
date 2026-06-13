# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isEqual(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def isEqual(self, root, subroot) -> bool:
        if not subroot and not root:
            return True
        
        if (subroot and not root) or (root and not subroot):
            return False

        if root.val != subroot.val:
            return False
        
        return self.isEqual(root.left, subroot.left) and self.isEqual(root.right, subroot.right)
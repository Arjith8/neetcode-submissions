# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # For in order traversal always the first value if the root node
        
        # That means if we have [1,2,3,4] we are confident that 1 is the root node
        # what about its left and right child
            # can i say that the value next to root in the array can i say that its gonna be left node
                # No lets say in Example 1 we didnt have the node which is 2 then list is [1,3,4]
                    # is node 3 the left root NO so we need something that can give this info
        
        # we know that in in order we look from left -> root -> right

        if not preorder or not inorder:
            return
        
        current = preorder[0]
        root = TreeNode(val = current)
        root_inorder_index = inorder.index(current)
        
        left_inorder = inorder[:root_inorder_index]
        right_inorder = inorder[root_inorder_index+1:]

        left_preorder = preorder[1:root_inorder_index+1]
        right_preorder = preorder[root_inorder_index+1:]

        # print(left_inorder, right_inorder)
        # print(left_preorder, right_preorder)
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root      
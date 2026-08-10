# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = root
        prev = None
        while node:
            print(node.val)
            if node.val == key:
                if prev is None:
                    if node.left is None:
                        root = node.right
                    elif node.right is None:
                        root = node.left
                    else:
                        new_head = node.left
                        right_node = node.right
                        node.left = node.right = None
                        abandoned_node = new_head.right
                        new_head.right = right_node
                        if abandoned_node:
                            ll_node = right_node
                            while ll_node.left:
                                ll_node = ll_node.left
                            
                            ll_node.left = abandoned_node
                        root = new_head
                else:
                    if node.left is None:
                        if node == prev.left:
                            prev.left = node.right
                        else:
                            prev.right = node.right
                    elif node.right is None:
                        if node == prev.left:
                            prev.left = node.left
                        else:
                            prev.right = node.left
                    else:
                        new_head = node.left
                        right_node = node.right
                        node.left = node.right = None
                        if node == prev.left:
                            prev.left = new_head
                        else:
                            prev.right = new_head

                        abandoned_node = new_head.right
                        new_head.right = right_node
                        if abandoned_node:
                            ll_node = right_node
                            while ll_node.left:
                                ll_node = ll_node.left
                            
                            ll_node.left = abandoned_node
                            
                break
            prev = node
            if node.val > key:
                node = node.left
            else:
                node = node.right

        return root
        
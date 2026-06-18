# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder - head -> left -> right

        # preorder we expect the first node/num of the list to be the head
        # whats the flaw with just having preorder
            # we dont know whether the subsequent node is left or head or right

        # inorder  - left -> head -> right
        # which means we know that the left side of the inorder list is gonna be left of head
        #  and right will be right

        # taking example of Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
        # from preorder we know that 1 is head
            # we dont know whether 2 is left side or right
        
        # so we refer to inorder so that we know at which index 1 is and everything towards
        #  its left is part of head.left
        # ie 1 head list to the left of 1 in inorder is [2] and that belongs in the left side
        # implied [3,4] belongs to right 

        if not preorder or not inorder:
            # assert preorder == inorder
            return None

        current = preorder[0]

        head = TreeNode(val=current)
        # print(preorder, inorder)
        for i in range(len(inorder)):
            if inorder[i] == current:
                break

        left_inorder = inorder[:i]
        right_inorder = inorder[i+1:]

        # print(current)
        left_preorder = preorder[1:i+1]
        right_preorder = preorder[i+1:]

        head.left = self.buildTree(left_preorder, left_inorder)
        head.right = self.buildTree(right_preorder, right_inorder)

        return head
        
        
                  
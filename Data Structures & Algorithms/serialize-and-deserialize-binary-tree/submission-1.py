# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        inter = []
        queue = collections.deque([[root, None]])
        while queue:
            current, parent = queue.popleft()
            inter.append(f"{getattr(current, 'val', None)}#{getattr(parent, 'val', None)}")
            if current:
                queue.append([current.left, current])
                queue.append([current.right, current])
        
        return "|".join(inter)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split('|')
        head_data_val = data[0].split("#")[0]
        if head_data_val == "None":
            return None
        head = TreeNode(val = head_data_val)
        queue = collections.deque([head])
        for i in range(1, len(data), 2):
            parent = queue.popleft()
            child_left_val = data[i].split("#")[0]
            child_right_val = data[i+1].split("#")[0]

            if child_left_val != "None":
                child_left = TreeNode(val=child_left_val)
                parent.left = child_left
                queue.append(child_left)
            
            if child_right_val != "None":
                child_right = TreeNode(val=child_right_val)
                parent.right = child_right
                queue.append(child_right)

        return head
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        root = Node(val=node.val)
        to_be_visited = [node]
        track = {node: root}
        while to_be_visited:
            current = to_be_visited.pop()
            if current not in track:
                temp = Node(val=current.val)
                track[current] = temp
            
            current_copied_node = track[current]
            for i in current.neighbors:
                if i not in track:
                    to_be_visited.append(i)
                    temp = Node(val=i.val)
                    track[i] = temp
                current_copied_node.neighbors.append(track[i])

        return root

        
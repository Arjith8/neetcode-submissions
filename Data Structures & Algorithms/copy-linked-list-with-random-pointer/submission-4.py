"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        track = {None: None}
        if not head:
            return None
        new_head = Node(x = head.val)
        track[head] = new_head
        while head:
            next_node = head.next
            if next_node:
                track[next_node] = track.get(next_node, Node(x=next_node.val))
                track[head].next = track[next_node]

            random_node = head.random
            if random_node:
                track[random_node] = track.get(random_node, Node(x=random_node.val))
                track[head].random = track[random_node]
            
            head = head.next
        return new_head

        
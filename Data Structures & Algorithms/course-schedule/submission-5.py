class Graph:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Solution:
            
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = {}
        visited = [False] * numCourses
        if not prerequisites:
            return True

        def build_graph(values):
            for i in values:

                if i[0] not in nodes:
                    node = Graph(i[0])
                    nodes[i[0]] = node
                
                node = nodes[i[0]]

                if i[1] not in nodes:
                    child_node = Graph(i[1])
                    nodes[i[1]] = child_node
                child_node = nodes[i[1]]

                node.add_child(child_node)
        
        def check_cycle(root):
            queue = collections.deque()
            queue.append(root)
            c = 0
            while queue:
                if c > numCourses+10:
                    return False
                current = queue.popleft()
                queue.extend(current.children)

                visited[current.val] = True
                c += 1
            
            return True
        
        graph_node = build_graph(prerequisites)
        resp = True
        for i in nodes:
            if not visited[i]:
                resp = resp and check_cycle(nodes[i])
        
        return resp
        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(set)
        for edge in edges:
            left, right = edge
            adj_list[left].add(right)
            adj_list[right].add(left)
        
        visited = set()
        def dfs(current, prev):
            if current in visited:
                return False
            
            visited.add(current)
            for i in adj_list[current]:
                if i != prev and not dfs(i, current):
                    return False
            
            return True
            
        return dfs(0, -1) and len(visited) == n
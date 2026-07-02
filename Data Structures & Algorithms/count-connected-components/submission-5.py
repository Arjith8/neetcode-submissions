class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        visited = set()
        count = 0
        def dfs(current, prev):
            if current in visited:
                return False
            
            visited.add(current)
            for i in adj_list[current]:
                if i != prev:
                    dfs(i, current)

            return True
        for i in adj_list:
            if dfs(i, -1):
                count +=1
            
        return count + n - len(visited)
        


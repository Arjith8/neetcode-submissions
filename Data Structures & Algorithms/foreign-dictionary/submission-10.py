class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {c: set() for w in words for c in w}

        for i in range(len(words)-1):
            first, second = words[i], words[i+1]
            min_len = min(len(first), len(second))
            if len(first) > len(second) and first[:min_len] == second[:min_len]:
                return ""

            for j in range(min_len):
                if first[j] != second[j]:
                    adj_list[first[j]].add(second[j])
                    break
        
        visited = {}
        output = []
        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node] = True

            for neighbour in adj_list[node]:
                if dfs(neighbour):
                    return True

            output.append(node)
            visited[node] = False
            return False
                    
        for i in adj_list:
            if dfs(i):
                return ""
            
        resp = "".join(output)
        return resp[::-1]
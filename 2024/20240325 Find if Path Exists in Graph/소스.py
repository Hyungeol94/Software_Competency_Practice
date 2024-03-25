class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False]*n
        mystack = [source]
        visited[source] = True
        adjacency_list = [[] for _ in range(n)]

        for edge in edges:
            k, v = edge
            adjacency_list[k].append(v)
            adjacency_list[v].append(k)

        def dfs(mystack):
            node = mystack[-1]
            if node == destination: 
                return True
            
            else:
                for next_node in adjacency_list[node]:
                    if not visited[next_node]:
                        mystack.append(next_node)
                        visited[next_node] = True
                        temp = dfs(mystack)
                        if temp == True:
                            return True
                        # visited[next_node] = False
                        
        return True if dfs(mystack) else False
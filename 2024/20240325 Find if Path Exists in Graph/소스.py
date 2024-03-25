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
            temp = mystack[-1]
            if temp == destination: 
                return True
            
            else:
                for edge in adjacency_list[temp]:
                    if not visited[edge]:
                        mystack.append(edge)
                        visited[edge] = True
                        return dfs(mystack)
                        visited[edge] = False
                        mystack.pop()

        return True if dfs(mystack) else False
import copy
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        visited = [False]*n
        visited[0] = True
        mystack = [0]
        answer = []

        def bfs():
            node = mystack[-1]
            if node == n-1:
                answer.append(mystack.copy())
            
            else:
                for next_node in graph[node]:
                    if not visited[next_node]:
                        mystack.append(next_node)
                        visited[next_node] = True
                        bfs()
                        mystack.pop()
                        visited[next_node] = False
        bfs()
        return answer                
from collections import defaultdict

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adjList = defaultdict(list)
        inDegrees = defaultdict(int)
        for k, v in relations:
            adjList[k].append(v)
            adjList[v] += []
            inDegrees[k] += 0
            inDegrees[v] += 1

        count = 0
        while inDegrees:
            found = False
            deleteList = []
            for node, neighbors in adjList.items():
                if node in inDegrees and inDegrees[node] == 0:
                    deleteList.append(node)
                    found = True
            
            for node in deleteList:
                for neighbor in adjList[node]:
                    inDegrees[neighbor] -= 1
                del inDegrees[node]

            if not found and len(inDegrees)!=0:
                return -1
            
            count += 1
        
        return count
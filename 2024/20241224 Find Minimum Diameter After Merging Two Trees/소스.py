from collections import defaultdict


from collections import deque

class Solution:
    def findDiameter(self, adj_list):
        degrees = {key : len(neighbors) for key, neighbors in adj_list.items()}
        myqueue = deque([key for key, degree in degrees.items() if degree == 1])
        if not myqueue:
            return 0

        count = 0
        while myqueue:
            count += 1
            #양파껍질 까기        
            next_queue = []
            while myqueue:
                curr = myqueue.popleft()
                if adj_list[curr]:
                    unique_neighbor = list(adj_list[curr])[0]
                    del adj_list[curr]
                    del degrees[curr]
                    if curr in adj_list[unique_neighbor]:
                        adj_list[unique_neighbor].remove(curr)
                    degrees[unique_neighbor] -= 1
                    if degrees[unique_neighbor] == 1:
                        next_queue.append(unique_neighbor)
            
            myqueue = deque(next_queue)

            if len(adj_list) == 1:
                return count * 2
            if len(adj_list) == 2:
                return count * 2 + 1

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        adj_list1 = defaultdict(set)
        adj_list2 = defaultdict(set)

        for edge in edges1:
            a, b = edge
            adj_list1[a].add(b)
            adj_list1[b].add(a)
        
        for edge in edges2:
            u, v = edge
            adj_list2[u].add(v)
            adj_list2[v].add(u)
        
        res1 = self.findDiameter(adj_list1)
        res2 = self.findDiameter(adj_list2)
        return max(res1, res2, math.ceil(res1/2) + math.ceil(res2/2) +1)
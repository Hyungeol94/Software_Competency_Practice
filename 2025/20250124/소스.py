#https://leetcode.com/problems/find-eventual-safe-states/
#Find Eventual Safe States

import heapq
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #outgoing edge로부터 거꾸로 줄어들면서 Kahn's algorithm으로 풀기
        #init
        n = len(graph)
        outgoing_list = [set() for i in range(n)]
        incoming_list = [set() for i in range(n)]
        heap = []
        heapq.heapify(heap)

        for i, neighbors in enumerate(graph):
            if not neighbors:
                heapq.heappush(heap, i)
            
            for neighbor in neighbors:
                outgoing_list[i].add(neighbor)
                incoming_list[neighbor].add(i)

        answer = set()
        while heap:
            curr = heapq.heappop(heap)
            answer.add(curr)
            for neighbor in incoming_list[curr]:
                if curr in outgoing_list[neighbor]:
                    outgoing_list[neighbor].remove(curr)
                    if not outgoing_list[neighbor]:
                        heapq.heappush(heap, neighbor)
                
        return sorted(list(answer))
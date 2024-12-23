
import heapq

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        for i, query in enumerate(queries):
            a, b = query
            if a > b:
                a, b = b, a
            queries[i] = [a,b]
        
        #끝나는 순으로 정렬한 쿼리
        sorted_queries = sorted([[i, *query] for i, query in enumerate(queries)], key = lambda a: -a[2])
        
        answer = [-1]*len(queries)
        min_heap = []
        heapq.heapify(min_heap)
        traversal_index = len(heights)-1
        for query in sorted_queries:
            i, a, b = query
            if a == b:
                answer[i] = a
                continue

            if heights[a] < heights[b]:
                answer[i] = b
                continue
            
            while b < traversal_index:
                heapq.heappush(min_heap, traversal_index)
                traversal_index -= 1
            
            while min_heap and heights[min_heap[0]] <= heights[b]:
                heapq.heappop(min_heap)

            temp = copy.deepcopy(min_heap)

            while temp and heights[temp[0]] <= heights[a]:
                heapq.heappop(temp)
            
            if not temp:
                answer[i] = -1
            else:
                answer[i] = temp[0]
        
        return answer
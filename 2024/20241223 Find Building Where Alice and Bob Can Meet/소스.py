
import heapq
import bisect
from collections import deque

class Solution:
    ##잘된 구현(leetcode)
    def search(self, height, mono_stack):
        left = 0
        right = len(mono_stack) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mono_stack[mid][0] > height:
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans

    ##잘못된 구현
    def binary_search(self, a, mono_stack):
        left = 0
        right = len(mono_stack)-1
        mid = (left+right) // 2

        while left <= right:
            mid = (left+right) // 2
            if a == mono_stack[mid][0]:
                return mid
            elif a > mono_stack[mid][0]:
                right = mid-1
            else:
                left = mid+1

        if left == 0:
            return left if a <= mono_stack[left][0] else -1
        return left

    def insert(self, stack, height, i):
        while stack and stack[-1][0] <= height:
            stack.pop()
        stack.append([height, i])

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        for i, query in enumerate(queries):
            a, b = query
            if a > b:
                a, b = b, a
            queries[i] = [a,b]
        
        #끝나는 순으로 정렬한 쿼리
        sorted_queries = sorted(
            [[i, *query] for i, query in enumerate(queries)], 
            key = lambda a: -a[2]
            )
        
        answer = [-1]*len(queries)
        mono_stack = []
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
                self.insert(mono_stack, heights[traversal_index], traversal_index)
                traversal_index -= 1 
                
            # index = self.binary_search(heights[a], mono_stack)
            index = self.search(heights[a], mono_stack)
            if 0 <= index < len(mono_stack):
                answer[i] = mono_stack[index][1]
            else:
                answer[i] = -1

        return answer
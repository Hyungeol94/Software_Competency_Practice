from collections import defaultdict 
from collections import deque
from typing import List

class Solution:
    def bfs(self, component, incoming_edges)-> int:
        depths = []
        for node in component:
            myqueue = deque([[node, 1]])
            seen = set(component)
            while myqueue:
                curr, depth = myqueue.popleft()
                for neighbor in incoming_edges[curr]:
                    if neighbor not in seen:
                        myqueue.append([neighbor, depth+1])
                        seen.add(neighbor)
            depths.append(depth)    
        
        return sum(depths)

    def maximumInvitations(self, favorite: List[int]) -> int:
        #1) kahn's algorithm으로 컴포넌트 찾기
        #2) 컴포넌트가 두개로 이루어져 있음 -> bfs
        #3) 컴포넌트가 여러 개로 되어 있음 -> 그 컴포넌트를 구성하는 노드의 수

        #kahn's algorithm 적용
        n = len(favorite)
        indegrees = [0]*n
        incoming_edges = [[] for _ in range(n)]
        for i, num in enumerate(favorite):
            indegrees[num] += 1
            incoming_edges[num].append(i)
        
        myqueue = deque([])
        for num, indegree in enumerate(indegrees):
            if not indegree:
                myqueue.append(num)
        
        while myqueue:
            curr = myqueue.popleft()
            dest = favorite[curr] 
            indegrees[dest] -= 1
            if not indegrees[dest]:
                myqueue.append(dest)
        print(indegrees)

        #컴포넌트 구하기
        seen = set()
        components = []
        for num, indegree in enumerate(indegrees):
            if not indegree:
                continue
            
            component = []
            curr = num
            while curr not in seen:
                seen.add(curr)
                component.append(curr)
                curr = favorite[curr]
            if component:
                components.append(component)

        #계산하기
        maxLen = 1
        acc = 0
        for component in components:
            if len(component) == 2:
                #상호참조의 경우, 중복해서 테이블에 넣을 수 있음
                acc += self.bfs(component, incoming_edges)
                
            else:
                #상호참조가 아닌 경우는 중복해서 넣을 수 없음
                maxLen = max(maxLen, len(component))
        
        return max(acc, maxLen)
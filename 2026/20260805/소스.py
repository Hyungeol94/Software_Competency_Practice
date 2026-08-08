#https://leetcode.com/problems/remove-methods-from-project/description/?envType=daily-question&envId=2026-08-05
#3310. Remove Methods From Project

from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for invocation in invocations:
            a, b = invocation
            adj_list[a].append(b)
        
        #k와 닿아있는 것들 체크
        #suspicious group
        suspicious_group = set([k])
        myqueue  = deque([k])
        while myqueue:
            curr = myqueue.popleft()
            for neighbor in adj_list[curr]:
                if neighbor in suspicious_group:
                    continue
                myqueue.append(neighbor)
                suspicious_group.add(neighbor)

        #외부 접촉 확인 
        seen = set([])
        is_removable = True
        for i in range(n):
            if i in suspicious_group:
                continue
            myqueue = deque([i])
            seen.add(i)
            while myqueue:
                curr = myqueue.popleft()
                for neighbor in adj_list[curr]:
                    if neighbor in seen:
                        continue
                    if neighbor in suspicious_group:
                        is_removable = False
                    seen.add(neighbor)
                    myqueue.append(neighbor)
        
        return list(range(n)) if not is_removable else list(seen-suspicious_group)
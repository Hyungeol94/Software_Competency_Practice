from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
            
        self.myqueue = deque([[0, '0000']])
        visited = set()
        def bfs():
            while self.myqueue:
                depth, curr = self.myqueue.popleft()
                if curr == target:
                    return depth
                
                for i, c in enumerate(curr):
                    newString = ''.join([str((int(c)+1)%10) if j == i else c for j, c in enumerate(curr)])
                    if newString not in deadends and newString not in visited:
                        visited.add(newString)
                        self.myqueue.append([depth+1, newString])
                    newString = ''.join([str((int(c)-1)%10) if j == i else c for j, c in enumerate(curr)])
                    if newString not in deadends and newString not in visited:
                        visited.add(newString)
                        self.myqueue.append([depth+1, newString])
        
        answer = bfs()
        return answer if answer!=None else -1
        
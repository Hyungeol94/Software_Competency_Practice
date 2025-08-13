#https://leetcode.com/problems/open-the-lock/
#752. Open the Lock

from collections import deque

class Solution:
    def add(self, a, b):
        return tuple([sum(nums) % 10 for nums in zip(a, b)])

    def openLock(self, deadends: List[str], target: str) -> int:
        drs = [(-1, 0, 0, 0), (1, 0, 0, 0), (0, -1, 0, 0), (0, 1, 0, 0), (0, 0, -1, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 0, 0, -1)]
        
        deadends_set = set([tuple([int(num) for num in deadend]) for deadend in deadends])
        visited = set()
        if (0, 0, 0, 0) in deadends_set:
            return -1

        myqueue = deque([[(0, 0, 0, 0), 0]])
        visited.add((0, 0, 0, 0))
        count = 0
        target_tuple = tuple([int(num) for num in target])

        while myqueue:
            count += 1
            curr, depth = myqueue.popleft()
            if curr == target_tuple:
                return depth
            for dr in drs:
                neighbor = self.add(curr, dr)
                if neighbor in deadends_set:
                    continue
                if neighbor in visited:
                    continue
                myqueue.append([neighbor, depth + 1])
                visited.add(neighbor)

        return -1
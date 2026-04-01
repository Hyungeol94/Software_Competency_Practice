#2751. Robot Collisions
#https://leetcode.com/problems/robot-collisions/description/?envType=daily-question&envId=2026-04-01

from collections import deque

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        arr = []
        for i, [pos, health, dr] in enumerate(zip(positions, healths, directions)):
            arr.append((pos, health, dr, i))
        
        arr.sort(key=lambda a: a[0])
        arr = deque(arr)
        ##LLLL RRRR 가능
        #LLLLL 가능
        #RRRRLLLL 안됨
        stack = []
        while arr:
            curr = arr.popleft()
            position, curr_health, curr_dr, curr_i = curr
            if curr_dr == 'R':
                stack.append(curr)
                continue

            #충돌
            while stack and stack[-1][2] == 'R' and stack[-1][1] < curr_health:
                stack.pop()
                curr_health -= 1

            if stack and stack[-1][2] == 'R':
                if stack[-1][1] == curr_health:
                    stack.pop()
                    continue
            
                if stack[-1][1] > curr_health:
                    prev_pos, prev_health, prev_dr, prev_i = stack[-1] 
                    stack.pop()
                    stack.append((prev_pos, prev_health-1, prev_dr, prev_i))
                    continue
            
            else:
                stack.append((position, curr_health, curr_dr, curr_i))

        stack.sort(key=lambda a: a[3])
        return list(map(lambda a: a[1], stack))
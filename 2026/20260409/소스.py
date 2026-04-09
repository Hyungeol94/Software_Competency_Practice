#https://leetcode.com/problems/walking-robot-simulation/?envType=daily-question&envId=2026-04-06
#874. Walking Robot Simulation

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        seen = set(map(lambda a: (a[0], a[1]), obstacles))
        drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        idx = 0
        curr = (0, 0)
        max_distance = 0

        for command in commands:
            if command == -2:
                idx = (idx-1) % 4
            elif command == -1:
                idx = (idx+1) % 4
            else:
                for i in range(command):
                    offset = drs[idx]
                    next_pos = (curr[0]+offset[0], curr[1]+offset[1])
                    if next_pos in seen:
                        break
                    curr = next_pos
                    max_distance = max(max_distance, next_pos[0]**2 + next_pos[1]**2)
        
        return max_distance
#https://leetcode.com/problems/robot-return-to-origin/?envType=daily-question&envId=2026-04-05
#657. Robot Return to Origin

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_offsets = {
            'R' : (0, 1),
            'L' : (0, -1),
            'U' : (-1, 0),
            'D' : (1, 0)
        }

        pos = [0, 0]
        for move in moves:
            offset = move_offsets[move]
            pos[0] += offset[0]
            pos[1] += offset[1]
        
        return True if pos[0] == 0 and pos[1] == 0 else False
            
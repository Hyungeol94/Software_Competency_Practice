#https://leetcode.com/problems/walking-robot-simulation-ii/?envType=daily-question&envId=2026-04-07
#2069. Walking Robot Simulation II

class Robot:
    def __init__(self, width: int, height: int):
        self._pos = [0, 0]
        self._dir_index = 0
        self._dir_offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self._dir_map =["East", "North", "West", "South"]
        self._width = width
        self._height = height

    def step(self, num: int) -> None:
        mod = (self._width-1)*2 + (self._height-1)*2
        if num % mod == 0:
            if self._pos == [0, 0]:
                self._dir_index = 3
        for _ in range(num % mod):
            offset = self._dir_offsets[self._dir_index]
            while not (0 <= self._pos[0] + offset[0] < self._width and 0 <= self._pos[1] + offset[1] < self._height):
                self._dir_index = (self._dir_index + 1) % 4
                offset = self._dir_offsets[self._dir_index]
            self._pos = [self._pos[0] + offset[0], self._pos[1] + offset[1]]
        
    def getPos(self) -> List[int]:
        return self._pos
        
    def getDir(self) -> str:
        return self._dir_map[self._dir_index]
        
        
# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
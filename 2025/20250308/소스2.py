#https://school.programmers.co.kr/learn/courses/30/lessons/250134
#[PCCP 기출문제] 4번 / 수레 움직이기

class Solution:
    def __init__ (self, maze):
        self.maze = maze #2차원 정수 뱌열
    
    def getMinTurns(self):
        self.minVal = float('inf')
        self.red_stack = []
        self.blue_stack = []
        self.red_visited = set()
        self.blue_visited= set()
        
        for i, row in enumerate(self.maze):
            for j, val in enumerate(row):
                if val == 1:
                    self.red_stack.append((i, j, 0))
                    self.red_visited.add((i, j)) ##시작 지점 방문 체크 꼭 하기
                if val == 2:
                    self.blue_stack.append((i, j, 0))
                    self.blue_visited.add((i, j, 0)) ##시작 지점 방문 체크 꼭 하기

        self.dfs()
        return self.minVal
        
        
    def dfs(self):
        drs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        red_i, red_j, red_depth = self.red_stack[-1]
        blue_i, blue_j, blue_depth = self.blue_stack[-1]
        n = len(self.maze)
        m = len(self.maze[0])
        
        if self.maze[red_i][red_j] == 3 and self.maze[blue_i][blue_j] == 4:
            self.minVal = min(self.minVal, max(red_depth, blue_depth))
        
        else:
            if self.maze[red_i][red_j] == 3: #붉은색 탐색 멈춤
                for dr in drs:
                    next_blue_i = blue_i + dr[0]
                    next_blue_j = blue_j + dr[1]
                    if not (0 <= next_blue_i < n and 0 <= next_blue_j < m):
                        continue

                    if (next_blue_i, next_blue_j) in self.blue_visited:
                        continue
                    
                    if self.maze[next_blue_i][next_blue_j] == 5: #벽 통과 못함
                        continue
                        
                    if next_blue_i == red_i and next_blue_j == red_j: #지나쳐갈 수 없음
                        continue

                    self.blue_visited.add((next_blue_i, next_blue_j))
                    self.blue_stack.append((next_blue_i, next_blue_j, blue_depth + 1))
                    self.dfs()
                    self.blue_visited.remove((next_blue_i, next_blue_j))
                    self.blue_stack.pop()
                # self.red_visited.remove((red_i, red_j))
                # self.red_stack.pop()
                
            
            elif self.maze[blue_i][blue_j] == 4: #푸른색 탐색 멈춤
                for dr in drs:
                    next_red_i = red_i + dr[0]
                    next_red_j = red_j + dr[1]
                    if not (0 <= next_red_i < n and 0 <= next_red_j < m):
                        continue

                    if (next_red_i, next_red_j) in self.red_visited:
                        continue
                    
                    if self.maze[next_red_i][next_red_j] == 5: #벽 통과 못함
                        continue
                    
                    if next_red_i == blue_i and next_red_j == blue_j: #지나쳐갈 수 없음
                        continue

                    self.red_visited.add((next_red_i, next_red_j))
                    self.red_stack.append((next_red_i, next_red_j, red_depth + 1))
                    self.dfs()
                    self.red_stack.pop()
                    self.red_visited.remove((next_red_i, next_red_j))
                # self.blue_visited.remove((blue_i, blue_j))
                # self.blue_stack.pop()
                
            
            else:
                for dr in drs:
                    next_blue_i = blue_i + dr[0]
                    next_blue_j = blue_j + dr[1]
                    if not (0 <= next_blue_i < n and 0 <= next_blue_j < m):
                        continue

                    if (next_blue_i, next_blue_j) in self.blue_visited:
                        continue
                    
                    if self.maze[next_blue_i][next_blue_j] == 5: #벽 통과 못함
                        continue
                        
                    self.blue_visited.add((next_blue_i, next_blue_j))
                    self.blue_stack.append((next_blue_i, next_blue_j, blue_depth + 1))

                    for dr in drs:
                        next_red_i = red_i + dr[0]
                        next_red_j = red_j + dr[1]
                        if not (0 <= next_red_i < n and 0 <= next_red_j < m):
                            continue

                        if (next_red_i, next_red_j) in self.red_visited:
                            continue
                    
                        if self.maze[next_red_i][next_red_j] == 5: #벽 통과 못함
                            continue

                        if next_blue_i == next_red_i and next_blue_j == next_red_j: #동시 방문 안됨
                            continue
                            
                        if next_blue_i == red_i and next_blue_j == red_j and next_red_i == blue_i and next_red_j == blue_j: #크로스 안됨
                            continue

                        self.red_visited.add((next_red_i, next_red_j))
                        self.red_stack.append((next_red_i, next_red_j, red_depth + 1))
                        self.dfs()
                        self.red_visited.remove((next_red_i, next_red_j))
                        self.red_stack.pop()
                    
                    self.blue_visited.remove((next_blue_i, next_blue_j))
                    self.blue_stack.pop()

                    
def solution(maze):
    instance = Solution(maze)
    res = instance.getMinTurns()
    return res if res != float('inf') else 0
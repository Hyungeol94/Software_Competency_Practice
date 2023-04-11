#https://www.acmicpc.net/problem/3190

import sys
from copy import deepcopy
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apple_matrix = []
for i in range(N+1):
    apple_matrix.append([False]*(N+1))

snake_matrix = deepcopy(apple_matrix)

for _ in range(K):
    y, x = list(map(int, sys.stdin.readline().split()))
    apple_matrix[y][x] = True

L = int(sys.stdin.readline())

commands = deque()
for _ in range(L):
    X, C = sys.stdin.readline().split()
    X = int(X)
    commands.append((X, C))

i = 0
snake_matrix[1][1] = True
game_on = True
direction = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
snake_x_position = 1
snake_y_position = 1
command_time, command = commands.popleft()
snake_positions = deque()
snake_positions.append((1,1))

while i != 10001 and game_on:
    current_snake_x_position = snake_x_position
    current_snake_y_position = snake_y_position

    next_snake_x_position = current_snake_x_position+ dx[direction]
    next_snake_y_position = current_snake_y_position+ dy[direction]

    #게임 멈추는 조건 확인
    if next_snake_x_position == N+1 or next_snake_x_position == 0 or next_snake_y_position == N+1 or next_snake_y_position == 0:
        game_on = False
        i += 1
        break

    if snake_matrix[next_snake_y_position][next_snake_x_position]:
        game_on = False

    snake_positions.append((next_snake_y_position, next_snake_x_position))
    #다음으로 이동하기
    snake_matrix[next_snake_y_position][next_snake_x_position] = True
    if apple_matrix[next_snake_y_position][next_snake_x_position]:
        apple_matrix[next_snake_y_position][next_snake_x_position] = False
    else:
        #꼬리가 없어져야 함
        tail_y_position, tail_x_position = snake_positions.popleft()
        snake_matrix[tail_y_position][tail_x_position] = False

    snake_x_position = next_snake_x_position
    snake_y_position = next_snake_y_position
    i += 1
    if i == command_time:
        #방향바꾸기
        if command == 'L':
            direction -= 1
            direction %= 4
        else:
            direction += 1
            direction %= 4
        if commands:
            command_time, command = commands.popleft()

print(i)


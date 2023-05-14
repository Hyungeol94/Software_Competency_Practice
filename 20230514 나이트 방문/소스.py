#코딩마스터스 6838. 나이트 방문

# 민규는 체스를 하고 있습니다. 그는 나이트를 이동시키면서 문득 다음과 같은 생각이 들었습니다.

# "이 나이트만 움직여서 모든 빈칸으로 이동할 수 있나?"

# 나이트의 이동 규칙은 다음과 같습니다.

# 편의상 체스판을 직교 좌표계로 나타내어 어떤 나이트가 (x, y)에 위치한다고 가정합시다.

# 그러면 그 나이트는 다음 8개의 좌표들 중 본인이 기물이 없는 체스판 위로 이동할 수 있습니다.

# (x-1, y+2), (x+1, y+2), (x-2, y+1), (x-2, y-1), (x+2, y-1), (x+2, y+1), (x-1, y-2), (x+1, y-2)

# 체스판의 상태가 주어질 때, 나이트만을 움직여서 모든 빈칸을 방문할 수 있는지 확인하는 프로그램을 작성해 주세요.

import sys
from collections import deque

matrix = []
visited = []
night_position = [-1, -1]
for i in range(8):
    input_string = sys.stdin.readline().strip()
    matrix.append(input_string)
    visited.append([False]*8)
    if 'N' in input_string:
        j = input_string.index('N')
        night_position = [i, j]

my_queue = deque()
my_queue.append(night_position)
i, j = night_position
visited[i][j] = True
dx = [-1, 1, -2, -2, 2, 2, -1, 1]
dy = [2, 2, 1, -1, -1, 1, -2, -2]
while my_queue:
    current_y_position, current_x_position = my_queue.popleft()
    for dy_i, dx_i in list(zip(dy, dx)):
        next_y_position = current_y_position+dy_i
        next_x_position = current_x_position+dx_i
        if next_y_position < 0 or 8 <= next_y_position or next_x_position < 0 or 8 <= next_x_position:
            continue
        if matrix[next_y_position][next_x_position] == 'W' or matrix[next_y_position][next_x_position] == 'N':
            visited[next_y_position][next_x_position] = True
            continue
        if visited[next_y_position][next_x_position]:
            continue
        my_queue.append([next_y_position, next_x_position])
        visited[next_y_position][next_x_position] = True

possible = "YES"
for line in visited:
    if False in line:
        possible = "NO"

print(possible)







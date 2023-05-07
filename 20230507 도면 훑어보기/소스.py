# 6843. 도면 훑어보기
# 기성이는 수많은 건물들의 설계 도면을 검사해야 합니다. 그러나 그 수가 너무나도 많아 일일이 확인하기엔 무리가 있습니다. 따라서 도면을 컴퓨터로 스캔한 뒤, 일정 기준을 충족하는 도면들만 추려내 검사하려고 합니다.

# 도면은 예시 입력과 같이 '.'와 '#' 두 가지 문자로만 이루어져 있으며, 각각 사람이 밟을 수 있는 바닥과 그렇지 않은 곳(벽, 기둥, 건물의 외부 등)을 의미합니다. 기성이가 확인하려는 조건은 다음과 같습니다.

# 1. 모든 '.'이 서로 연결되어 있다. 어떤 두 '.'이 연결되어 있다는 것은, 한 '.'에서 출발해 상하좌우로 인접한 다른 '.'를 통해 1번 이상 이동하여 다른 '.'에 도달할 수 있음을 의미한다.

# 2. 6칸 이상의 '#'이 서로 연결되어 있으며 이 덩어리는 '.'로 둘러싸여있다. 어떤 두 '#'이 연결되어 있다는 것은, 한 '#'에서 출발해 상하좌우로 인접한 다른 '#'를 통해 1번 이상 이동하여 다른 '#'에 도달할 수 있음을 의미한다.

# 입력으로 도면이 주어지면, 위 조건을 만족하는지 판별하는 프로그램을 작성해 주세요.

import sys
from collections import deque


def sharps_bfs(matrix, i, j, visited):
    # 6개 연달아 연결되어 있으면 return True
    # els return False
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    my_queue = deque()
    my_queue.append((i, j))
    count = 1
    visited[i][j] = True

    while my_queue:
        current_x_position, current_y_position = my_queue.popleft()
        for i in range(4):
            next_x_position = current_x_position + dx[i]
            next_y_position = current_y_position + dy[i]
            if next_x_position < 1 or 9 <= next_x_position or next_y_position < 1 or 19 <= next_y_position:
                continue
            if not visited[next_x_position][next_y_position] and matrix[next_x_position][next_y_position] == '#':
                my_queue.append((next_x_position, next_y_position))
                visited[next_x_position][next_y_position] = True
                count += 1

    if count >= 6:
        return True
    return False

def surrounded(matrix, i, j):
    # 점에 의해 둘러싸여져 있으면 됨
    surrounded_by_dots = True

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    visited = []
    for _ in range(10):
        visited.append([False] * 20)

    my_queue = deque()
    my_queue.append((i, j))
    count = 1
    visited[i][j] = True

    while my_queue:
        current_x_position, current_y_position = my_queue.popleft()
        for i in range(4):
            next_x_position = current_x_position + dx[i]
            next_y_position = current_y_position + dy[i]
            if next_x_position < 1 or 9 <= next_x_position or next_y_position < 1 or 19 <= next_y_position:
                continue
            if not visited[next_x_position][next_y_position] and matrix[next_x_position][next_y_position] == '#':
                my_queue.append((next_x_position, next_y_position))
                visited[next_x_position][next_y_position] = True
                if next_x_position == 1 or next_x_position == 8 or next_y_position == 1 or next_y_position == 18:
                    surrounded_by_dots = False

    return surrounded_by_dots


def dots_bfs(matrix, i, j, visited):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    my_queue = deque()
    my_queue.append((i, j))
    visited[i][j] = True

    while my_queue:
        current_x_position, current_y_position = my_queue.popleft()
        for i in range(4):
            next_x_position = current_x_position+dx[i]
            next_y_position = current_y_position+dy[i]
            if next_x_position < 0 or 10 <= next_x_position or next_y_position < 0 or 20 <= next_y_position:
                continue
            if not visited[next_x_position][next_y_position] and matrix[next_x_position][next_y_position] == '.':
                my_queue.append((next_x_position, next_y_position))
                visited[next_x_position][next_y_position] = True


def dots_connected(matrix):
    visited = []
    for _ in range(10):
        visited.append([False] * 20)

    flag = False
    for i in range(10):
        if flag:
            break
        for j in range(20):
            if matrix[i][j] == '.':
                dots_bfs(matrix, i, j, visited)
                flag = True
                break

    connected = True
    for i in range(10):
        for j in range(20):
            if matrix[i][j] == '.' and not visited[i][j]:
                connected = False
    return connected


def sharps_connected(matrix):
    visited = []
    for _ in range(10):
        visited.append([False] * 20)

    connected_and_surrounded = False
    for i in range(1, 9):
        for j in range(1, 19):
            if matrix[i][j] == '#' and not visited[i][j]:
                if sharps_bfs(matrix, i, j, visited) and surrounded(matrix, i, j):
                    connected_and_surrounded = True

    return connected_and_surrounded


def calculate():
    matrix = []
    for _ in range(10):
        matrix.append(sys.stdin.readline().strip())

    connected_dots = dots_connected(matrix)
    connected_sharps = sharps_connected(matrix)
    if not connected_dots and not connected_sharps:
        print(0)
    if connected_dots and not connected_sharps:
        print(1)
    elif not connected_dots and connected_sharps:
        print(2)
    elif connected_dots and connected_sharps:
        print(3)

K = int(sys.stdin.readline().strip())
for _ in range(K):
    calculate()

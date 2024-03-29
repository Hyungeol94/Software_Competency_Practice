def isValid(x, y, n):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def constructable(info, matrix):
    x, y, construct, command = info
    n = len(matrix[0])
    if construct:  # 보
        # 밑에 기둥이 있다면 true
        if x == n-1:
            return False
        if isColumnSupported(x,y,n,matrix):
            return True
        if isColumnSupported(x+1, y, n, matrix):
            return True
        # 양 옆에 보가 있다면 true
        if isBarrageSupported(x,y,n,matrix) and isBarrage(x+1, y, n, matrix):
            return True
    else:  # 기둥
        # 바닥이라면 true
        if y == n-1:
            return False
        if y == 0:
            return True
        #밑에 기둥이 있다면
        if isColumnSupported(x,y,n,matrix):
            return True
        # 밑에 보가 있다면 True
        if isBarrageSupported(x, y, n, matrix):
            return True
        if isBarrage(x,y,n,matrix):
            return True
    return False

def build(info, matrix):
    x, y, structure, _ = info
    n = len(matrix[0])
    if structure: #1일 때 보 짓기
        matrix[0][x][y] = 1
        matrix[1][x + 1][y] = 1

    else: #기둥 짓기
        matrix[2][x][y] = 1
        matrix[3][x][y + 1] = 1



def isBarrage(x, y, n, matrix): #보가 설치되어 있는지
    if isValid(x, y, n) and matrix[0][x][y] == 1:
        return True
    if y == 0:
        return True
    return False


def isBarrageSupported(x,y,n, matrix): #닿아있는 보가 있는지
    if isValid(x,y,n) and matrix[1][x][y] == 1:
        return True
    if y == 0:
        return True
    return False


def isColumn(x,y,n, matrix): #기둥이 설치되어 있는지
    if isValid(x,y,n) and matrix[2][x][y] == 1:
        return True
    return False


def isColumnSupported(x,y,n, matrix): #닿아있는 기둥이 있는지
    if isValid(x,y,n) and matrix[3][x][y] == 1:
        return True
    if y == 0:
        return True
    return False

def destructable(info, matrix):
    x, y, structure, command = info
    n = len(matrix[0])
    #보 위에 세워진 기둥이 있다면, 아래에 기둥이 더 있는지
    #0은 기둥 1은 보
    #단방향이므로 가능

    if structure: #destruct barrage
    # 보의 왼쪽 교차점 위에 세워진 기둥이 있는가
        if isColumn(x,y,n,matrix):
        #왼쪽 교차점 아래에 기둥이 없고, 왼쪽 교차점과 연결된 보가 없으면 return False
            if not (isColumnSupported(x,y,n, matrix) or isBarrageSupported(x, y, n, matrix)):
                return False

    # 보의 오른쪽 교차점 위에 세워진 기둥이 있는가
        if isColumn(x+1, y, n, matrix):
            #오른쪽 교차점 아래에 기둥이 없고, 오른쪽 교차점과 연결된 보가 없으면 return False
            if not (isColumnSupported(x+1, y, n, matrix) or isBarrage(x+1, y, n , matrix)):
                return False

    # 왼쪽 교차점과 연결된 보가 있다면, 그 보의 아랫쪽에 지탱해주는 기둥이 하나라도 있는지
        if isBarrageSupported(x,y,n,matrix):
            if not (isColumnSupported(x-1, y, n, matrix) or isColumnSupported(x, y, n, matrix)):
                return False

    # 오른쪽 교차점과 연결된 보가 있다면, 그 보의 아랫쪽에 지탱해주는 기둥이 하나라도 있는지
        if isBarrage(x+1, y, n, matrix):
            if not (isColumnSupported(x+1, y, n, matrix) or isColumnSupported(x+2, y, n, matrix)):
                return False
        return True

    else: #기둥일 때
        #기둥 위에 세워진 기둥이 있는가
        if isColumn(x, y+1, n, matrix):
            if not (isBarrageSupported(x, y+1, n, matrix) or isBarrage(x, y+1, n, matrix)):
                return False

        #기둥 위에 왼쪽 방향으로 세워진 보가 있는가
        if isBarrageSupported(x,y+1,n,matrix):
            #기둥 위에 왼쪽 방향으로 세워진 보를 지탱하는 다른 기둥이 없을 때
            if not isColumnSupported(x-1, y+1, n, matrix):
                #그 보를 지탱하는 다른 보가 양쪽에 있어야 함
                if not (isBarrage(x, y+1, n, matrix) and isBarrageSupported(x-1, y+1, n, matrix)):
                    return False


        #기둥 위에 오른쪽 방향으로 세워진 보가 있는가
        if isBarrage(x, y+1, n, matrix):
            # 기둥 오른쪽으로 연결된 보를 지탱하는 다른 기둥이 없을 때
            if not isColumnSupported(x+1, y+1, n, matrix):
                # 그 보를 지탱하는 다른 보가 양쪽에 있어야 함
               if not (isBarrage(x+1, y+1, n, matrix) and isBarrageSupported(x, y+1, n, matrix)):
                   return False
        return True

def destruct(info, matrix):
    x, y, structure, _ = info
    n = len(matrix[0])
    if structure:  # 보 파괴
        matrix[0][x][y] = -1
        matrix[1][x + 1][y] = -1
    else: #기둥 파괴
        matrix[2][x][y] = -1
        matrix[3][x][y + 1] = -1


def solution(n, build_frame):
    # 3차원 matrix 선언하기
    matrix = [[[-1 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(4)]
    #barrage_departure, barrage_destination, column_departure, column_departure
    #0은 기둥 1은 보
    for info in build_frame:
        x, y, _, command = info
        if command:  # 설치
            if constructable(info, matrix):
                build(info, matrix)

        else:  # 삭제
            if destructable(info, matrix):
                destruct(info, matrix)

    answer = []
    for i in range(n + 1):
        for j in range(n + 1):
            if matrix[0][i][j] == 1:  # 보 출발지점
                answer.append([i, j, 1])  # 보
            if matrix[2][i][j] == 1:  # 기동 출발지점
                answer.append([i, j, 0])  # 기둥
    answer.sort()
    return answer
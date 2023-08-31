#https://school.programmers.co.kr/learn/courses/30/lessons/160585#

def winning(mark, board):
    for row in board:
        if row.count(mark) == 3:
            return True
    for col in zip(*board):
        if col.count(mark) == 3:
            return True

    #내려가는 대각선 확인
    downward_diagonal = [board[i][i] for i in range(3)]
    if downward_diagonal.count(mark) == 3:
        return True
    
    #올라가는 대각선 확인
    upward_diagonal = [board[i][2-i] for i in range(3)]
    if upward_diagonal.count(mark) == 3:
        return True
    return False
    
def solution(board):
    O_count = 0
    X_count = 0
    for i, row in enumerate(board):
        for j, mark in enumerate(row):
            if mark == 'O':
                O_count += 1
            if mark == 'X':
                X_count += 1
    
    #O와 X를 번갈아서 하는 상황, O가 먼저임
    if O_count < X_count:
    #번갈아서 수를 두는 상황이기 때문에 X가 O보다 많을 수 없음
        return 0
    
    elif O_count > X_count:
    #O가 X+1보다 클 수 없음
        if not O_count == X_count+1:
            return 0     
        #X가 이긴다면 게임이 종료되었어야 하기 때문에 위 조건을 충족할 수 없음
        if winning('X', board):
            return 0
        
    elif O_count == X_count:
        if winning('O', board):
            return 0 
        #X가 이길 때는 같아도 괜찮음
    
    #둘 다 이기는 경우도 안됨
    if winning('O', board) and winning('X', board):
        return 0
    
    return 1
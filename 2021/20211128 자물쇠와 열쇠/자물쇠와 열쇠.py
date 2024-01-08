#20211127 토요일
##// (M+2N-2)*(M+2N-2) 크기의 배열 square 생성
##// (N-1, N-1) 위치에 M*M 크기 lock을 addup 하기
##// (0,0)부터 (M+N-2, M+N-2)위치까지 key_A, ..., key_D를 addup 후 lock에 빈틈이 없는지 체크 → return true
##// (i) key_A, key_B, key_C, key_D를 생성한 후
##// (ii)다시 addup하는 알고리즘을 짜야 함
##// 모든 탐색이 끝난 후에는 return false */

def solution(key, lock):
    ##// (M+2N-2)*(M+2N-2) 크기의 배열 square 생성
    M = len(key);
    N = len(lock);
    square = [];    
    for i in range(M+2*N-2):
        square.append([0]*(M+2*N-2));
    
    ##// (M-1, M-1) 위치에 N*N 크기 lock을 addup 하기
    for (r,i) in enumerate(range(M-1,M-1+N)):
        for (c,j) in enumerate(range(M-1,M-1+N)):
            square[i][j] += lock[r][c];

    answer = True
    current_key = key
    for k in range(5):
        #rotate_key #왼쪽방향으로 회전
        rotated_key = []
        for i in range(M):
            rotated_key.append([0]*M);

        for i in range(M):
            for j in range(M):
                rotated_key[M-j-1][i] = current_key[i][j];

        current_key = rotated_key

        
        #탐색시작
        ##square 상에서(0,0)부터 (M+N-2, M+N-2)위치까지 key_A, ..., key_D를
        ##addup 후lock에 빈틈이 없는지 체크 → return true
        
        for r in range(M+N-1):
            for c in range(M+N-1):
                addup_table = []
                for i in range(len(square)):
                    addup_table.append([])
                    for j in range(len(square)):
                        addup_table[i].append(square[i][j])

#key 크기(M*M)의 배열만큼 addup_table에 addup
                for i in range(M):
                    for j in range(M):
                        addup_table[r+i][c+j] += rotated_key[i][j]
                        if addup_table[r+i][c+j] >= 2:
                            break;

#lock에 빈틈이 없는지 체크 → return true        
                answer = True

                for i in range(M-1,M-1+N):
                    for j in range(M-1,M-1+N):
                        if ((addup_table[i][j] == 0) | (addup_table[i][j] == 2)):
                            answer = False;
                            break;

                if answer == True:
                    return answer
   
    return answer

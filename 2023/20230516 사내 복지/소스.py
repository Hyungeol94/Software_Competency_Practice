#6878. 사내 복지
# 어느 추운 겨울 날, 스타트업의 CEO 기성이는 직원들이 추위에 떨며 근무하는 모습에 마음이 아팠습니다. 사무실에 전열기 등의 난방기구가 전혀 없다는 것을 깨달은 기성이는 급하게 전열기 3개를 주문하였습니다. 이제 세 전열기를 사무실에 적절하게 배치하려고 합니다.
#
# 사무실은 N행 M열, 총 N × M칸의 격자로 나눌 수 있습니다. 각 칸에는 직원이 최대 한 명 근무하고 있습니다. i행 j열에 위치한 칸과 k행 l열에 위치한 칸 사이의 거리는 (i - k 의 절댓값) + (j - l 의 절댓값)과 같습니다. 직원들은 각 전열기와의 거리의 합 만큼 추위를 느낀다고 합니다. 예를 들어 한 직원이 (1, 1)에서 근무중이고 세 전열기가 (2, 2), (3, 4), (3, 6)에 설치되었다고 합시다. 이 직원은 14(= 2 + 5 + 7)만큼의 추위를 느끼게 됩니다.
#
# 전열기를 설치할 위치는 직원이 있는 칸이여도 되고, 심지어 이미 다른 전열기가 설치되어 있는 칸이여도 됩니다. 사무실의 크기와 직원들의 위치가 주어지면, 전열기 3개를 설치한 뒤 직원들이 느끼는 추위의 합의 최솟값을 출력하는 프로그램을 작성해 주세요.


import sys


def coldness(i, j, heater_positions):
    coldness_quantity = 0
    for y, x in heater_positions:
        coldness_quantity += abs(y-i)+abs(x-j)
    return coldness_quantity


def calculate_coldness(heater_positions, matrix, N, M, coldness_quantity):
    sum_coldness = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                sum_coldness += coldness(i, j, heater_positions)
    coldness_quantity[0] = min(coldness_quantity[0], sum_coldness)


def dfs(N, M, i, my_stack, matrix, coldness_quantity):
    if len(my_stack) == 3:
        #flatten된 좌표 값을 원래되로 복귀시키기
        heater_positions = []
        for number in my_stack:
            x = number // M
            y = number % M
            heater_positions.append([x, y])
        #print(heater_positions)
        calculate_coldness(heater_positions, matrix, N, M, coldness_quantity)

    else:
        for j in range(i, N*M):
            my_stack.append(j)
            dfs(N, M, j, my_stack, matrix, coldness_quantity)
            my_stack.pop()


N, M = list(map(int, sys.stdin.readline().split()))
matrix = []
for i in range(N):
    matrix.append([int(i) for i in sys.stdin.readline().strip()])

#print(matrix)
coldness_quantity = [1000000000]

#모든 가능한 히터 포지션들을 구하기
my_stack = []
dfs(N, M, 0, my_stack, matrix, coldness_quantity)

print(coldness_quantity[0])

#1은 직원이 있는 위치
#전열기 3개를 설치해 보자
#전열기 3개를 설치할 수 있는 모든 조합을 구해야 함








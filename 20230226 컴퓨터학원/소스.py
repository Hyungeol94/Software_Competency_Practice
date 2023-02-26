def func_1(i):
    if i != 1:
        return func_1(i-1)+func_2(i-1)
    if i == 1:
        return 2

def func_2(i):
    if i != 1:
        return func_1(i-1)*2 + func_2(i-1)
    if i == 1:
        return 3

import sys

#이건 bfs로 모든 가능성을 재면 되지 않을까?
#분명 timeout의 가능성이 있기 때문에 DP로 해결하는 게 제일 안전함


(N) = int(sys.stdin.readline())
print(func_2(N))
# 6849. 밑장 빼기
# 준하는 영화 "타짜"를 감명깊게 봤습니다. 영화에 나오는 손기술을 연습하던 준하는 카드더미에서 맨 윗장 뿐만이 아니라, 맨 아래에 있는 카드를 대신 내려놓는 기술을 쓸 수 있게 되었습니다!
# 1부터 N까지 수가 쓰여져 있는 N장의 카드 더미가 주어집니다. 이 카드 더미에서 맨 위 또는 맨 아래에 있는 카드를 내려놓는 것을 반복해서, 1부터 N까지 차례대로 내려놓을 수 있는지 알려주는 프로그램을 작성해 주세요.

import sys

N = sys.stdin.readline()
num_list = list(map(int, sys.stdin.readline().split()))
number = 1
flag = True
while num_list:
    if num_list[-1] == number:
        num_list.pop()
        number += 1
        continue
    elif num_list[0] == number:
        num_list.pop(0)
        number += 1
        continue
    flag = False
    break

if flag:
    print("YES")
else:
    print("NO")

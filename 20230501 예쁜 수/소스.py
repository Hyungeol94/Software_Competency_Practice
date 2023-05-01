#코딩마스터스 6851. 예쁜 수
# 어떤 수가 그 수의 "부분 수"로 나누어 떨어지면 이 수를 "예쁜 수"라고 합니다.

# "부분 수"란, 수의 맨앞과 맨뒤에서 총 1개 이상의 숫자를 떼어내어 만든 수를 말합니다.

# 예를 들어, 13은 11349의 "부분 수"이고, 11349는 13으로 나누어 떨어지므로 "예쁜 수"입니다.

# 어떤 수가 주어지면, 이 수가 "예쁜 수"인지 여부를 출력하는 프로그램을 작성해 주세요.

import sys
N = sys.stdin.readline().strip()
pretty = False
for i in range(len(N)-1):
    for j in range(i, len(N)):
        if i == 0 and j == len(N)-1:
            continue
        if int(N)%int(N[i:j+1])==0:
            pretty = True

if pretty:
    print('YES')
else:
    print('NO')
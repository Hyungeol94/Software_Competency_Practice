#코딩마스터스 6853. 팰린드롬 만들기
# 팰린드롬은 역순으로 읽어도 같은 낱말을 뜻합니다. 예를 들어, "EYE", "MADAM"은 팰린드롬이지만 "APPLE", "CODE"는 아닙니다.
# 여러분에게 문자열들이 주어집니다. 이 문자열들을 적절히 재배열해서, 하나의 팰린드롬 문자열을 만들 수 있는지 여부를 출력하는 프로그램을 작성해 주세요.

import itertools
import sys

def check_palindrom(string_list):
    candidate = ''.join(string_list)
    length = len(candidate)
    for i in range(length//2):
        if candidate[i] != candidate[length-1-i]:
            return False
    return True


N = int(sys.stdin.readline())
strings = []
for _ in range(N):
    strings.append(sys.stdin.readline().strip())

FOUND = False
for x in itertools.permutations(strings, N):
    if check_palindrom(list(x)):
        FOUND = True

if FOUND:
    print('YES')
else:
    print('NO')




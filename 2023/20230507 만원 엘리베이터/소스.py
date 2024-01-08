# 코딩마스터스 6842. 만원 엘리베이터
# 기성이는 굉장히 급한 업무가 생겼습니다. 그것은 바로 방금 도착한 중요한 서류를 가능한 빨리 임원에게 전달하는 것입니다. 기성이가 일하는 사무실은 빌딩의 2층에 있고, 임원의 집무실은 꼭대기 층이기 때문에 엘리베이터를 타야만 합니다. 엘리베이터의 문이 열리자, 엘리베이터를 가득 채운 직장동료 N명이 나타났습니다. 기성이는 어떻게든 같이 타려고 했지만, 정원 초과라는 경고음과 함께 엘리베이터가 출발하지 않았습니다.
# 기성이의 사정을 이해한 직원들은 정확히 한 명이 내려서 기성이를 대신 태워주기로 했습니다. 각 직원은 체중 X와 바쁜 정도 Y라는 두 가지 정수를 가지고 있습니다. 엘리베이터가 출발하기 위해선 (N명의 체중의 합) - (내린 사람의 체중) + (기성이의 체중)이 엘리베이터가 수용 가능한 최대 무게 K보다 크지 않아야 합니다. 기성이에게 자리를 양보하여 엘리베이터를 출발하게 할 수 있는 직원을 모두 출력하는 프로그램을 작성해 주세요.

import sys

N, M, K = map(int, sys.stdin.readline().split())
data = []
weight_sum = 0
for _ in range(N):
    weight, business = map(int, sys.stdin.readline().split())
    weight_sum += weight
    data.append((weight, business))

data.sort(key=lambda a: (a[1], -a[0]))
answer = []
for weight, business in data:
    if weight_sum - weight + M <= K:
        answer.append((weight, business))

print(len(answer))
for weight, business in answer:
    print(weight, business)
import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))

answer = []
for i in range(1, min(data) + 1):
    equal = True
    k = data[0] % i
    for j, datum in enumerate(data):
        if datum % i != k:
            equal = False
    if equal:
        answer.append(i)

for i in answer:
    print(i, end=' ')

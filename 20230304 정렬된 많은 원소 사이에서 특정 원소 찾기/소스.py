import sys

(N, A) = list(map(int, sys.stdin.readline().split()))
data = list(map(int, sys.stdin.readline().split()))

i = 0
Found = False
while not Found and (i != N):
    if data[i] == A:
        Found = True
        break
    i += 1
if not Found:
    print(-1)
else:
    print(i+1)

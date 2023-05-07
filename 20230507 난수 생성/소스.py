#6880. 난수 생성
import sys

X, A, B, C, N = map(int, sys.stdin.readline().split())
for _ in range(N):
    X = (X*A+B) % C

print(X)
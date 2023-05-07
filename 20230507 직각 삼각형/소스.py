#6881. 직각 삼각형
import sys

a,b,c = map(int, sys.stdin.readline.split())
longest = max(a,b,c)
smallest = min(a,b,c)
other = a+b+c-longest -smallest
if longest**2 == smallest**2 + other**2:
    print('YES')
else:
    print('NO')
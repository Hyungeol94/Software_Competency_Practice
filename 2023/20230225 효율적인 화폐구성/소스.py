import sys


def dfs(N,
        M,
        point,
        depth):
    global min_depth, found
    if M == point:
        min_depth = depth
        found = True
        return

    if M < point:
        min_depth = min(min_depth, depth)
        return

    else:
        for i in range(N):
            if not found:
                point += data[i]
                dfs(N, M, point, depth + 1)
                point -= data[i]


global min_depth
min_depth = 10001
found = False

(N, M) = list(map(int, sys.stdin.readline().split()))
data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))

data.sort(reverse=True)

dfs(N, M, 0, 0)
if not found:
    print(-1)
else:
    print(min_depth)

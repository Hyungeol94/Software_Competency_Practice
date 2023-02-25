import sys

def dfs(N,
        M,
        point,
        depth):
    global min_depth
    if M <= point:
        min_depth = min(min_depth, depth)
        return

    else:
        for i in range(N):
            point += data[i]
            dfs(N, M, point, depth+1)
            point -= data[i]


global min_depth
min_depth = 10001

(N, M) = list(map(int, sys.stdin.readline().split()))
data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))

dfs(N, M, 0, 0)
print(min_depth)


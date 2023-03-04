import sys

(n) = int(sys.stdin.readline())

tile = []
tile.append(1)
tile.append(2)
for i in range(2,n):
    tile.append(tile[-1] + tile[-2])

print(tile[n-1] % 796796)
import sys

(n) = int(sys.stdin.readline())
data = []
if n == 1:
    print(3)
elif n == 2:
    print(7)
else:
    data = [2, 2, 3]

    # 셋째 i = 2
    i = 2
    while i != n:
        temp = []
        temp.append(data[0] + data[2])
        temp.append(data[0] + data[2])
        temp.append(data[0] + data[1] + data[2])
        data = temp.copy()
        i += 1

    print(sum(data) % 796796)





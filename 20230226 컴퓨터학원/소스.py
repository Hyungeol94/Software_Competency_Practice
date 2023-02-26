import sys
(n) = int(sys.stdin.readline())
data = []
if n == 1:
    print(3)
elif n == 2:
    print(7)
else:
    data = [2,2,3]

    #셋째 i = 2
    i = 2
    while i != n:
        temp = []
        for datum in data:
            if datum == 2:
                temp.append(2)
                temp.append(3)
            else:
                temp.append(2)
                temp.append(2)
                temp.append(3)
        i += 1
        data = temp.copy()
    print(sum(data))





import sys
a = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().strip().split()))
numbers_length = len(numbers)

count = 1
while count < numbers_length:
    count *= 2

while len(numbers) != count:
    numbers.append(0)

stack = []
stack.append(numbers)

while len(numbers) != 1:
    temp = []
    limit = len(numbers)
    i = 0
    while i != limit:
        temp.append(numbers[i] + numbers[i + 1])
        i += 2
    numbers = temp
    stack.append(numbers)

while stack:
    temp = stack.pop()
    for (index, i) in enumerate(temp):
        if index == len(temp):
            print(i, end = '')
            break
        print(i, end = ' ')
    print()
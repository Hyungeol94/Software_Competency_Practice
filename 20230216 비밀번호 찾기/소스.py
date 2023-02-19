import sys
a = (sys.stdin.readline())
a = ''.join(a.split())

index = -1
for i, letter in enumerate(a):
    if letter == 'c':
        index = i
        break;

for i in (a[:index+1]):
    if i == a[:index+1]:
        print(i, end = '')
        break
    print(i, end = ' ')

#6882. 피보나치 피보나치 수열
import sys
#(1 ≤ a, b ≤ 100)

a, b = map(int, sys.stdin.readline().split())
fibo = [1,1,2]
i = 0
while i != 100:
    fibo.append(fibo[-1]+fibo[-2])
    i+=1

fibofibo = []
for i in range(25):
    for j in range(fibo[i]):
        fibofibo.append(fibo[i])

fibo_sum = 0
for i in range(a-1, b):
    fibo_sum+=fibofibo[i]

print(fibo_sum)








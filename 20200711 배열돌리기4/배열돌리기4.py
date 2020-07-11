

#중복 안됨
def dfs(depth):
    global temp, n, m, k, visited, mystack
    if (depth == k):
        #매트릭스 복사, 해보고 안되면 한행씩 복사하
        temp = [0]*n
        for i in range(n):
            temp[i] = [0]*m
            for j in range(m):
                temp[i][j] = matrix[i][j]
            
        for i in range(k):
            #연산
            rotate(mystack[i])
        calculate()
            
    else:
        for i in range(k):
            if visited[i] == True:
                continue;
            else:
                visited[i] = True
                mystack.append(command[i])
                dfs(depth+1)
                mystack.pop()
                visited[i] = False
                

def rotate(dd):
    (r,c,k) = dd
    r-= 1
    c-= 1
    
    #temp 배열을 회전시키고 계산하기
    global temp
    #if right, (r-s, c-s) to (r-s, c+s)
    for s in range(1, k+1):
        buffer = temp[r-s][c-s]
        for i in range(c-s, c+s):
            buffer2 = temp[r-s][i+1]
            temp[r-s][i+1] = buffer
            buffer = buffer2

        #if down, (r-s, c+s) to (r+s, c+s)
        for i in range(r-s, r+s):
            buffer2 = temp[i+1][c+s]
            temp[i+1][c+s] = buffer
            buffer = buffer2
            
        #if left, (r+s, c+s) to (r+s, c-s)
        for i in reversed(range(c-s+1, c+s+1)):
            buffer2 = temp[r+s][i-1]
            temp[r+s][i-1] = buffer
            buffer = buffer2
            
        #if up, (r+i, c-i) to (r-i, c-i)
        for i in reversed(range(r-s+1, r+s+1)):
            buffer2 = temp[i-1][c-s]
            temp[i-1][c-s] = buffer
            buffer = buffer2
        

def calculate():
    global n, m, k, temp, answer;
    for i in range(n):
        temp_sum = 0
        for j in range(m):
            temp_sum += temp[i][j]
        if answer > temp_sum:
            answer = temp_sum
    

temp = input().split()
(n, m, k) = [int(i) for i in temp]
matrix = []
temp = []
answer = 10000

for i in range(n):
    temp = input().split()
    matrix.append([int(j) for j in temp])

command = []
for i in range(k):
    temp = input().split()
    command.append([int(j) for j in temp])

mystack = []
visited = [False]*k  
dfs(0)
print(answer)
    
    
    
    

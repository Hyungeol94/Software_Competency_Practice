n = int(input())
temp = input()
data = [i for i in temp]
numbers = []
operators = []
for i in range(len(data)):
    if (i%2 == 0):
        numbers.append(int(data[i]))
    else:
        operators.append(data[i])
        
mystack = []
visited = [False]*len(operators)
import pdb
summ = [-2147483648]

def calculate(mystack):
    #pdb.set_trace()
    duplicate = []
    bracket = []
    snd_cal = []
    dupp_stack = []
    temp_numbers = []

    for i in range(len(numbers)):
            temp_numbers.append(numbers[i])
    
    myqueue = []
    next_operator = []
    
    i =0;
    while(i!=len(mystack)):
        if operators[i] == '+':
            if mystack[i] == True: #계산만하기
                temp = numbers[i]+numbers[i+1]
                temp_numbers[i] = temp
                temp_numbers[i+1] = temp
                if (i == len(mystack)-1):
                    myqueue.append(temp)
                
            else: #다음을 준비
                myqueue.append(temp_numbers[i])
                next_operator.append(operators[i])
                if (i == len(mystack)-1):
                    myqueue.append(temp_numbers[i+1])
                
        elif operators[i] == '-':
            if mystack[i] == True:
                temp = numbers[i]-numbers[i+1]
                temp_numbers[i] = temp
                temp_numbers[i+1] = temp
                if (i == len(mystack)-1):
                    myqueue.append(temp)
            else:
                myqueue.append(temp_numbers[i])
                next_operator.append(operators[i])
                if (i == len(mystack)-1):
                    myqueue.append(temp_numbers[i+1])
                
            
        elif operators[i] == '*':
            if mystack[i] == True:
                temp = numbers[i]*numbers[i+1]
                temp_numbers[i] = temp
                temp_numbers[i+1] = temp
                if (i == len(mystack)-1):
                    myqueue.append(temp)
            else:
                myqueue.append(temp_numbers[i])
                next_operator.append(operators[i])
                if (i == len(mystack)-1):
                    myqueue.append(temp_numbers[i+1])
        i+=1


    buffer = myqueue[0]
    i = 0;
    #pdb.set_trace()
    while(i!=len(next_operator)):
        temp = next_operator[i]
        if temp == '+':
            buffer = buffer+myqueue[i+1]
            
        elif temp == '-':
            buffer = buffer-myqueue[i+1]
            
        elif temp == '*':
            buffer = buffer*myqueue[i+1]
        i += 1
    
    if buffer >= summ[0]:
        #pdb.set_trace()
        summ[0] = buffer
        

#연산 순서를 정하는 것이지만,
#괄호 밖에 있는 연산자들은 그 순서가 이미 정해져 있어야 한다.
        
def dfs(depth):
    if (depth == len(operators)):
        #print(*mystack)
        calculate(mystack)

    else:
        #pdb.set_trace()
        for i in [True, False]:
            if (len(mystack)!=0):
                if(mystack[-1]==True) & (i == True):
                    continue;
                mystack.append(i)
            else:
                mystack.append(i)
            dfs(depth+1)
            mystack.pop()
                            
            
if (n>1):
    dfs(0)
else:
    summ[0] = data[0]
print(summ[0])
   

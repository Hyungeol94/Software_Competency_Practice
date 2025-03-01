#https://school.programmers.co.kr/learn/courses/30/lessons/340210


# k진법으로 변환하는 함수
def convert_to_decimal(k, num):
    multiplier = 1
    value = 0
    for c in str(num)[::-1]:
        value += int(c) * multiplier
        multiplier *= k
        
    return value

#k진법으로 바꾸기
def convert_from_decimal(k, num):
    denominator = k ** 10
    ans = []
    while 1 <= denominator:
        res = num // denominator
        ans.append(str(res))
        num = num - (res * denominator)
        denominator //= k
    
    return int(''.join(ans))
    

## 진법의 범위를 계산하는 함수
def update_range(arr, candidates):
    operator = arr[1]
    new_candidates = []
    for k in candidates:
        operand1 = convert_to_decimal(k, arr[0]) 
        operand2 = convert_to_decimal(k, arr[2])
        result = convert_to_decimal(k, arr[-1])
        if operator == "+":
            if operand1 + operand2 == result:
                new_candidates.append(k)
            else:
                continue
        elif operator == "-" :
            if operand1 - operand2 == result:
                new_candidates.append(k)
            else:
                continue
                
    return new_candidates

def get_results(candidates, num1, num2, operator):
    results = set()
    for candidate in candidates:
        num1_converted = convert_to_decimal(candidate, num1)
        num2_converted = convert_to_decimal(candidate, num2)
        if operator == "+":
            results.add(convert_from_decimal(candidate, num1_converted+num2_converted))
        else:
            results.add(convert_from_decimal(candidate, num1_converted-num2_converted))
    return list(results)
        

def solution(expressions):
    #2~9진법 중 하나임
    #사용된 모든 표현들의 집합으로 해당 진법 내의 최대 digit을 찾을 수 있음(진법의 범위 찾기)
    #결과값이 있고, 그 결과값이 십진법인 경우의 결과와 다른 경우 유추 가능
        #ex) 51 - 5 = 44에서 이 문명이 사용하던 진법이 8진법임을 알 수 있습니다. 
        #1) 십진법과 다른지 확인한다
        #2) 진법 찾기 -> brute force로 확인 가능 
    #해당 결과값이 현재 가능한 진법의 범위 내에서 판단 가능한 경우   -> 그 값으로 채워넣기
    #해당 결과값이 현재 가능한 진법의 범위 내에서 판단 불가능한 경우 -> ? 처리하기
    #ex) 1 + 2 = X의 결괏값은 6 ~ 9진법에서 모두 3으로 같습니다. 따라서 1 + 2 = X의 지워진 결괏값을 채워 넣으면 1 + 2 = 3이 됩니다.
    #ex) 1 + 5 = X의 결괏값은 6진법일 때 10, 7 ~ 9진법일 때 6이 됩니다.
    
    numSet = set()
    for expression in expressions:
        for c in expression:
            if c.isnumeric():
                numSet.add(int(c))
    
    ## 진법의 범위 업데이트
    i = max(numSet)
    j = 10
    candidates = list(range(i+1, j))
    for expression in expressions:
        # 결과값이 없는 것은 skip
        if expression[-1] == "X":
            continue
        
        #진법의 결과가 십진법과 다른 경우, 진법의 범위를 업데이트하기
        arr = expression.split()
        operator = arr[1]
        if operator == "+":
            if int(arr[0]) + int(arr[2]) == int(arr[4]): #십진법과 같은 경우
                continue
            else: #십진법과 다른 경우
                candidates = update_range(arr, candidates)
                
                
        else: #operator == "-":
            if int(arr[0]) - int(arr[2]) == int(arr[4]):
                continue
            else:
                candidates = update_range(arr, candidates)
    
    
    ## ?를 채워넣기
    ans = [] 
    for i, expression in enumerate(expressions):
        if expression[-1] != "X":
            continue
        
        arr = expression.split()
        operator = arr[1]
        results = get_results(candidates, arr[0], arr[2], operator)        
        if len(results) == 1:
            ans.append(expressions[i][:-1] + str(results[0]))
        else:
            ans.append(expressions[i][:-1] + "?")
    
    return ans
#https://school.programmers.co.kr/learn/courses/30/lessons/77884

def get_submultiple(number):
    count = 0
    for n in range(1, number+1):
        if number % n == 0:
            count += 1
    return count

def isEven(number):
    if number %2 == 0:
        return True
    return False

def solution(left, right):
    answer = 0
    for number in range(left, right+1):
        submultiple_number = get_submultiple(number)
        if isEven(submultiple_number):
            answer += number
        else:
            answer -= number
    return answer    
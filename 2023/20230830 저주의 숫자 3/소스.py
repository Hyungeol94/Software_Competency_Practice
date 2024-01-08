#https://school.programmers.co.kr/learn/courses/30/lessons/120871

def is_unfortunate(i):
    if (i%3 == 0) or ('3' in str(i)):
        return True
    else:
        return False

def next_number(i):
    while True:
        i += 1
        if not is_unfortunate(i):
            return i       

def solution(n):
    converted_number = 0
    for _ in range(n):
        converted_number = next_number(converted_number)
    return converted_number

            
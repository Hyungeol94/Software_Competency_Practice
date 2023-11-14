#https://school.programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations
from collections import deque


def operate(left, right, operand):
    if operand == '+':
        return int(left) + int(right)
    if operand == '-':
        return int(left) - int(right)
    if operand == '*':
        return int(left) * int(right)


def calculate(operand, expression):
    new_expression = []
    expression = deque(expression)
    while expression:
        item = expression.popleft()
        if item != operand:
            new_expression.append(item)
            continue
        left = new_expression.pop()
        right = expression.popleft()
        new_expression.append(operate(left, right, item))
    return new_expression

def compute(order, expression):
    # 순서에 맞게 계산하기
    for operand in order:
        expression = calculate(operand, expression)
    return expression[0]


def parse_expression(expression):
    number = ''
    parsed_expression = []
    for char in expression:
        if char not in '-*+':
            number = number + char
        else:
            parsed_expression.append(number)
            parsed_expression.append(char)
            number = ''
    parsed_expression.append(number)
    return parsed_expression


def solution(expression):
    parsed_expression = parse_expression(expression)
    operands = ['*', '+', '-']
    answer = 0
    for order in permutations(operands, 3):
        answer = max(answer, abs(compute(order, parsed_expression)))
    
    return answer
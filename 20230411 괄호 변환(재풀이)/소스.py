#https://school.programmers.co.kr/learn/courses/30/lessons/60058
# 2020 KAKAO BLIND RECRUITMENT 기출문제

def proper(u):
    if u[0] == ')':
        return False
    stack = []
    stack.append(u[0])
    i = 0
    while stack and i != len(u) - 1:
        i += 1
        if u[i] != stack[i - 1]:
            stack.pop()
    if i != len(u) - 1:
        return False
    return True


def solution(p):
    stack = []
    stack.append(p[0])
    i = 0
    while stack and i != len(p) - 1:
        i += 1
        if p[i] != stack[i - 1]:
            stack.pop()
    u = p[:i + 1]
    v = p[i + 1:]

    if proper(u):
        return u + solution(v)
    else:
        temp_string = '(' + solution(v) + ')'
        reverse_u = ''
        for j in u[1:-1]:
            if j == '(':
                reverse_u += ')'
            else:
                reverse_u += '('
        return temp_string + reverse_u

    return answer
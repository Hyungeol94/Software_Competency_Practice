#https://school.programmers.co.kr/learn/courses/30/lessons/17681


def number_to_byte(number, n):
    converted_number = bin(number)[2:]
    if len(converted_number) < n:
        converted_number = '0'*(n-len(converted_number))+converted_number
    return converted_number
    
    
def convert(arr, n):
    new_arr = list(map(
        lambda x: number_to_byte(x, n)
        , arr))
    return new_arr


def solution(n, arr1, arr2):
    arr1 = convert(arr1, n)
    arr2 = convert(arr2, n)
    matrix = []
    for i, [str1, str2] in enumerate(zip(arr1, arr2)):
        arr = []
        for j, [c1, c2] in enumerate(zip(str1, str2)):
            if c1 == '1' or c2 == '1':
                arr.append('#')
            else:
                arr.append(' ')
        matrix.append(''.join(arr))
    return matrix
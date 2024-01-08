#https://level.goorm.io/exam/195687/이진수-정렬/quiz/1
def convert_to_binary(numerator):
	if numerator == 0:
		return '0'
	
	denominator = 2**20
	
	while True:
		if numerator//denominator == 1:
			break
		denominator //= 2

	binary_numbers = []
	while denominator!= 0:
		binary_numbers.append(numerator//denominator)
		numerator = numerator%denominator
		denominator = denominator//2
	
	return ''.join(list(map(str, binary_numbers)))
	

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(key=lambda a: (-convert_to_binary(a).count('1'), -a))
print(numbers[K-1])




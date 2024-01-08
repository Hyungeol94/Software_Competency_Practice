# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def add_values(values, next_row, next_col, value):
	values[next_row][next_col] += value

def is_valid(number, n):
	if 0<=number and number<n:
		return True
	return False

def compute(matrix, row, col, n, values):
	d_row = [0, 0, -1, 0, 1]
	d_col = [0, 1, 0, -1, 0]
	for dr, dc in zip(d_row, d_col):
		next_row = row+dr-1
		next_col = col+dc-1
		if is_valid(next_row, n) and is_valid(next_col, n):
			if matrix[next_row][next_col]!='#':
				add_values(values, next_row, next_col, 2) if matrix[next_row][next_col] == '@' else add_values(values, next_row, next_col, 1)
	
		
n, k = map(int, input().split())
matrix = []
values = []

for i in range(n):
	matrix.append(input().split())
	values.append([0]*n)
		
for _ in range(k):
	row, col = list(map(int, input().split()))
	compute(matrix, row, col, n, values)

	
maximum = 0

for i in range(n):
	for j in range(n):	
			if values[i][j]>maximum:
				maximum = values[i][j]
print(maximum)
			

	
#https://level.goorm.io/exam/195689/구름-찾기-깃발/quiz/1

def is_valid(number, N):
	if number<0 or N<=number:
		return False
	return True

def mark(i, j, info, matrix, N):
	d_row = [0, -1, -1, -1, 0, 1, 1, 1]
	d_col = [1, 1, 0, -1, -1, -1, 0, 1]
	count = 0
	for row, col in zip(d_row, d_col):
		next_row = i+row
		next_col = j+col
		if is_valid(next_row, N) and is_valid(next_col, N):
			if info[next_row][next_col] == 1:
				count += 1
	matrix[i][j] = count
						

N, K = map(int, input().split())
info= []
matrix = []
for i in range(N):
	info.append(list(map(int, input().split())))
	matrix.append([0]*N)

for i in range(N):
	for j in range(N):
		if info[i][j] == 0:
			mark(i,j, info, matrix, N)

count = 0
for i in range(N):
	for j in range(N):
		if matrix[i][j] == K:
			count += 1

print(count)
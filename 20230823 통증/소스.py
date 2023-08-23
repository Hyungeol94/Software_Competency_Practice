#https://level.goorm.io/exam/195690/통증/quiz/1

N = int(input().strip())
numerator = N
denominators=[0,1,7,14]
denominator = 14
count = 0
while True:
	if denominator == 0:
		break
	count += numerator//denominator
	numerator %= denominator
	denominator = denominators[denominators.index(denominator)-1]
print(count)


	
	

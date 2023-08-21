#https://level.goorm.io/exam/195688/문자열-나누기/quiz/1

N = int(input().strip())
string = input().strip()
substrings = []
for i in range(1, len(string)-1):
	for j in range(i+1, len(string)):
		substrings.append(string[0:i])
		substrings.append(string[i:j])
		substrings.append(string[j:])

substrings = sorted(list(set(substrings)))
point = 0

for i in range(1, len(string)-1):
	for j in range(i+1, len(string)):
		point = max(point, substrings.index(string[0:i])+substrings.index(string[i:j])+substrings.index(string[j:])+3)

print(point)

								 

		
	
	

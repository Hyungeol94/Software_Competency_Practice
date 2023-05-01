#6850. 치팅 검사
#대학교 조교인 준하는 과제를 채점하고 있습니다. 그런데 채점하던 도중, 다른 학생과 비슷한 답안을 쓴 학생이 있다는 사실을 알게 되었습니다. 여러가지 조사를 한 준하는 다음과 같은 사실을 알아냈습니다. 치팅을 한 과제는 정상적인 답안을 둘로 나누어, 앞과 뒤를 한번씩 더 반복하는 방식으로 쓰여져 있었습니다. 예를 들어, 정상적인 답안이 "ABCD"라면, 치팅을 한 과제는 "ABABCDCD", "AABCDBCD"와 같은 방식으로 쓰여져 있습니다. 어느 학생의 과제 답안이 주어졌을 때, 치팅을 했는지 여부와, 원래 답안을 출력하는 프로그램을 작성해 주세요.

import sys

def check(char_string):
    char_length = len(char_string)
    if char_string[:char_length//2] == char_string[char_length//2:]:
        return True
    return False

char_string = sys.stdin.readline().strip()
char_length = len(char_string)
CHEATED = False
answer = ''
for i in range(char_length):
    if check(char_string[:i]) and check(char_string[i:]):
        CHEATED = True
        answer = char_string[:i//2]+char_string[i:i+(char_length-i)//2]

if CHEATED:
    print('YES')
    print(answer)
else:
    print('NO')


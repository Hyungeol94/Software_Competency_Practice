#6847. 단어 퍼즐
# 길이가 3인 단어 6개가 주어집니다. 이 단어들을 이용해 3 x 3 크기의 낱말 퍼즐을 만드는 프로그램을 작성해 주세요.
# 출력한 3 x 3 크기의 낱말 퍼즐에는 가로로 읽은 단어 3개와, 세로로 읽은 단어 3개가 입력으로 주어진 6개의 단어와 일대일로 매칭되어야 합니다.

import sys
import itertools

def is_puzzle(word_combination):
    word_matrix = [word_combination[0], word_combination[1], word_combination[2]]
    for i in range(3):
        word = word_matrix[0][i] + word_matrix[1][i] + word_matrix[2][i]
        if word != word_combination[i+3]:
            return False
    return True

def print_puzzle(word_combination):
    for i in range(3):
        print(word_combination[i])

word_list = []
for _ in range(6):
    word_list.append(sys.stdin.readline().strip());

answer_list = []
for word_combination in itertools.permutations(word_list, 6):
    if is_puzzle(list(word_combination)):
        answer_list.append(word_combination)

answer_list.sort()
print_puzzle(answer_list[0])

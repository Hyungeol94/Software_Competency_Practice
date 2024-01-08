#https://school.programmers.co.kr/learn/courses/30/lessons/120869

from itertools import permutations
def solution(spell, dic):
    letters = list(set(spell))
    for word in permutations(letters):
        if ''.join(word) in dic:
            return 1
    return 2
    
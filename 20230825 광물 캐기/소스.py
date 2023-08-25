from itertools import permutations

def calculate_exhaustion(block, dick):
    if dick == 'dia':
        return len(block) 
    elif dick == 'iron':
        return block.count('diamond')*5+block.count('iron')+block.count('stone')
    elif dick == 'stone':
        return block.count('diamond')*25+block.count('iron')*5+block.count('stone')
    
def calculate_scores(x, minerals):
    left = 0
    right = 5 if 5<=len(minerals) else len(minerals)
    score = 0
    index = 0
    while True:
        block = minerals[left:right]
        score += calculate_exhaustion(block, x[index])
        left = right
        right = right+5 if right+5<=len(minerals) else len(minerals)
        index += 1
        if index == len(x):
            break
        if left ==right:
            break
    return score
        
def solution(picks, minerals):
    dia, iron, stone = picks
    len_blocks = len(minerals)//5 
    if len(minerals)%5!=0:
        len_blocks+=1
    capa = dia+iron+stone
    coverage = picks
    if len_blocks<=capa:
        coverage = [0, 0, 0]
        index = 0
        while sum(coverage) != len_blocks and index != 3:
            data = picks[index] if sum(coverage)+picks[index]<len_blocks else len_blocks-sum(coverage)
            coverage[index] = data
            index += 1
    print(coverage)
    #조합을 찾기
    minimum = 1000000000000000000
    for x in permutations(['dia']*coverage[0]+['iron']*coverage[1]+['stone']*coverage[2], sum(coverage)):
        minimum = min(minimum, calculate_scores(x, minerals))

    return minimum
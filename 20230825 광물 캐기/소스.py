#https://school.programmers.co.kr/learn/courses/30/lessons/172927

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
    return score

def dfs(depth, coverage, mystack, dick_dict, minimum, minerals, criteria):
    if depth == criteria:
        minimum[0] = min(minimum[0], calculate_scores(mystack, minerals))
    
    else:
        for i in range(3):
            if coverage[i]!=0:
                mystack.append(dick_dict[i])
                coverage[i] -= 1
                dfs(depth+1, coverage, mystack, dick_dict, minimum, minerals, criteria)
                mystack.pop()
                coverage[i] += 1
            
      
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
            
    #조합을 찾기
    minimum = [1000000000000000000]
    mystack = []
    dick_dict = {0:'dia', 1:'iron', 2:'stone'}
    dfs(0, coverage, mystack, dick_dict, minimum, minerals, sum(coverage))

    return minimum[0]

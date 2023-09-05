def isConditionMet(subsequence, gems_unique):
    gems_check = [False]*len(gems_unique)
    for item in subsequence:
        if item in gems_unique:
            gems_check[gems_unique.index(item)] = True
    if False in gems_check:
        return False
    return True
 
    
def solution(gems):
    gems_unique = list(set(gems))
    gems_length = len(gems_unique)
    for current_size in range(gems_length, len(gems)+1):
        #size만큼 확인 -> 계속해서 업데이트 해주기
        for j in range(0, len(gems)+1-current_size):
            subsequence = gems[j:j+current_size]
            if isConditionMet(subsequence, gems_unique):
                return [j+1, j+current_size]
    
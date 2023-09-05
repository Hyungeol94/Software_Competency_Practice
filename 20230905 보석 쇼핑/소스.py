#https://school.programmers.co.kr/learn/courses/30/lessons/67258?language=python3
def isConditionMet(gems_check):
    if False in gems_check:
        return False
    return True


def solution(gems):
    gems_unique = list(set(gems))
    gems_check = [False ] *len(gems_unique)
    left = 0
    right = 0
    subsequence = [gems[0]]
    gems_check[gems_unique.index(gems[0])] = True
    answer = []

    while True:
        # 조건에 부합한다면, answer에 저장하기
        if isConditionMet(gems_check):
            answer.append([left+1, right+1])

        # 종료조건 설정 -> 일단 right이 끝이어야 함 & 줄이기 시작할 때 작아져야 함
        if right == len(gems) - 1:
            if set(gems[left:]) - set(gems[left + 1:]) != set({}):
                break

        if right != len(gems) - 1:
            right += 1

        # subsequence 확장
        subsequence.append(gems[right])

        # check해주기
        gems_check[gems_unique.index(gems[right])] = True
        # 왼쪽 걸 빼도 되는지 확인하고, 빼도 되면 빼기
        while set(gems[left:right+1] ) -set(gems[left+1:right+1] )==set({}):
            if subsequence != []: subsequence.pop(0)
            left += 1

    answer.sort( key=lambda a: (a[1]-a[0], a[0]))
    return answer[0]




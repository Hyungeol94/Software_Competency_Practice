#https://school.programmers.co.kr/learn/courses/30/lessons/67258?language=python3


def isConditionMet(subsequence_dict, gems_unique):
    if len(subsequence_dict) == len(gems_unique):
        return True
    return False


def solution(gems):
    gems_unique = list(set(gems))
    left = 0
    right = 0
    answer = []
    #실제로 subsequence가 return 값에 포함되지 않으므로 subsequence 전체를 가지고 있을 필요는 없음
    #한편, 조건에 부합하는지의 여부를 효율적으로 확인할 수 있는 다른 유형의 자료 구조를 활용할 것이 요구됨
    #dictionary 구조가 적합 <- 조회, 삭제에 O(1)의 시간 복잡도를 가지기 때문

    subsequence_dict = {}
    #subsequence_dict[gems[0]] = 1
    command = 'expand'
    while True:
        # 종료조건 설정
        # right이 끝에 도달했지만 조건을 만족하지 않을 때 -> left을 더 올려도 소용 없는 상황
        if right == len(gems) and not isConditionMet(subsequence_dict, gems_unique):
            break

        command = 'expand' if len(subsequence_dict) < len(gems_unique) else 'shrink'
        if command == 'expand':
            while not isConditionMet(subsequence_dict, gems_unique) and right != len(gems):
                subsequence_dict[gems[right]] = subsequence_dict[gems[right]] + 1 if subsequence_dict.get(gems[right]) else 1
                right += 1
            if isConditionMet(subsequence_dict, gems_unique):
                answer.append([left+1, right])

        if command == 'shrink':
            while isConditionMet(subsequence_dict, gems_unique) and left<= right:
                if subsequence_dict.get(gems[left]) and subsequence_dict[gems[left]]  >= 2:
                    subsequence_dict[gems[left]] = subsequence_dict[gems[left]] -1
                else:
                    del subsequence_dict[gems[left]]
                if not isConditionMet(subsequence_dict, gems_unique):
                    answer.append([left+1, right])
                left += 1

    answer.sort( key=lambda a: (a[1]-a[0], a[0]))
    return answer[0]

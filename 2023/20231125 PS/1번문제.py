import itertools

def solution(friends, gifts):
    #두 사람간의 선물기록 관리하기 -> matrix로 관리하기
    #준 선물만 기록하면 됨
    #선물지수 관리하기 -> dict로 관리

    n = len(friends)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    rate_dict = {}
    for record in gifts:
        A, B = record.split()
        # 선물기록 관리
        i = friends.index(A)
        j = friends.index(B)
        matrix[i][j] += 1
        # 선물지수 관리
        rate_dict[A] = rate_dict[A]+1 if rate_dict.get(A) else 1
        rate_dict[B] = rate_dict[B]-1 if rate_dict.get(B) else -1

    #matrix와 rate_dict를 가지고, 다음달에 받을 선물의 수를 예측하기
    predict_dict = {}
    for i, (A, B) in enumerate(itertools.combinations(friends, 2)):
        #두 사람 간에 비교해서, 누가 선물을 받는지 예측
        #두 사람 간에 기록이 있을 때
        #print(A, B)
        i = friends.index(A)
        j = friends.index(B)
        if (matrix[i][j] != 0 or matrix[j][i]!=0) and matrix[i][j] != matrix[j][i]:
            if matrix[i][j] > matrix[j][i]:
                predict_dict[A] = predict_dict[A]+1 if predict_dict.get(A) else 1
            else:
                predict_dict[B] = predict_dict[B]+1 if predict_dict.get(B) else 1
            continue
        #선물 지수를 비교하기
        A_rate = rate_dict[A] if rate_dict.get(A) else 0
        B_rate = rate_dict[B] if rate_dict.get(B) else 0
        if A_rate > B_rate:
            predict_dict[A] = predict_dict[A]+1 if predict_dict.get(A) else 1
        elif A_rate < B_rate:
            predict_dict[B] = predict_dict[B]+1 if predict_dict.get(B) else 1
        else: #선물지수도 같음
            continue

    answer = list(sorted(predict_dict.items(), key= lambda a: -a[1]))
    return answer[0][1] if answer else 0

#print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
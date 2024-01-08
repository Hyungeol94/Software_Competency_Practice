#https://www.acmicpc.net/problem/9547

#후보 C명, 유권자 V명
#유권자 수만큼, 후보에 대한 선호도가 주어짐
#1후보 수만큼의 선호도가 나옴. 중복은 없음
#투표는 2회에 걸쳐 진행됨
import math

def calculate():
    num_candidates, num_voters = map(int, input().split());
    sum_scores = [0]*num_candidates

    ##1회차 투표
    ranks = []
    for _ in range(num_voters):
        rank = list(map(int, input().split()));
        ranks.append(rank)
        # 가장 처음 주어지는 후보가 가장 선호하는 후보이며
        # 가장 마지막에 주어지는 후보가 가장 선호하지 않는 후보
        selected_candidate_id = rank[0]
        sum_scores[selected_candidate_id-1] += 1

    winning_number = math.ceil(num_voters/2)
    for candidate_id, sum_score in enumerate(sum_scores):
        if sum_score >= winning_number:
            print(candidate_id+1, 1)
            return

    ##2회차 투표
    candidate_scores = list(zip([i+1 for i in range(num_candidates)], sum_scores))
    candidate_scores.sort(key=lambda a: (a[1]), reverse=True)
    competing_candidates = list(zip(*candidate_scores[:2]))[0]
    competing_candidates_scores =[0, 0]
    for rank in ranks:
        if rank.index(competing_candidates[0]) < rank.index(competing_candidates[1]):
            competing_candidates_scores[0] += 1
        else:
            competing_candidates_scores[1] += 1
    if competing_candidates_scores[0] > competing_candidates_scores[1]:
        print(competing_candidates[0], 2)
        return
    print(competing_candidates[1], 2)
    return


num_cases = int(input())
for T in range(num_cases):
    calculate()



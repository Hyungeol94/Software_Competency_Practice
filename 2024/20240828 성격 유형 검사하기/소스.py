from collections import defaultdict

def solution(survey, choices):
    dist = defaultdict(int)
    for item, choice in zip(survey, choices):
        if choice in [1,2,3]:
            dist[item[0]] += (4-choice)
        elif choice == 4:
            continue
        else:
            dist[item[1]] += choice-4
    
    answer = ''
    answer += 'T' if dist['R'] < dist['T'] else 'R'
    answer += 'F' if dist['C'] < dist['F'] else 'C'
    answer += 'M' if dist['J'] < dist['M'] else 'J'
    answer += 'N' if dist['A'] < dist['N'] else 'A'
    return answer
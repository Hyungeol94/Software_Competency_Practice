import itertools

def dfs(mystack, n, depth, count, A_choice_indices, B_choice_indices, dice):
    if (depth == n):
        a_sum, b_sum = 0, 0
        for i in range(n//2):
            A_dime = dice[A_choice_indices[i]-1]
            a_sum += A_dime[mystack[i]]
        for j in range(n//2):
            B_dime = dice[B_choice_indices[j]-1]
            b_sum += B_dime[mystack[j+n//2]]
        if a_sum > b_sum:
            count[0] += 1

    else:
        for i in range(6):
            mystack.append(i)
            dfs(mystack, n, depth+1, count, A_choice_indices, B_choice_indices, dice)
            mystack.pop()
def winning_count(A_choice_indices, dice):
    n = len(dice)
    B_choice_indices = tuple(set(range(1, n+1))-set(A_choice_indices))
    mystack = []
    count = [0]
    dfs(mystack, n, 0, count, A_choice_indices, B_choice_indices, dice)
    return count


def solution(dice):
    n = len(dice)
    indices = [i for i in range(1, n+1)]
    choice = [0, 0]
    max_winning_count = -1

    for A_choice_indices in itertools.combinations(indices, n//2):
        count = winning_count(A_choice_indices, dice)
        if max_winning_count < count[0]:
            max_winning_count = count[0]
            choice = A_choice_indices
    return list(choice)

#print(solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]))
#print(solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]))
#print(solution([[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]))
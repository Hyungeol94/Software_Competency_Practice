#https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    t = 0
    left = -1
    right = 0
    right_max = len(sequence)-1
    #10만번 딱 한 번 훑을 수 있어야 함
    subsequence_sum = sequence[0]
    command = 'expand'
    answer = []
    while True:
        subsequence_sum -= sequence[left] if left >= 0 else 0
        left += 1

        if right < left or left == len(sequence):
            break

        command = 'expand' if subsequence_sum < k else 'shrink'

        #expand
        if command == 'expand':
            while True:
                if k <= subsequence_sum:
                    break
                right += 1
                if right == len(sequence):
                    right = len(sequence)-1
                    break
                subsequence_sum += sequence[right]

        #shrink
        if command == 'shrink':
            while True:
                if subsequence_sum <= k:
                    break
                subsequence_sum -= sequence[right]
                right -= 1

        if subsequence_sum == k:
            answer.append([left, right])



    answer.sort(key = lambda a:(a[1]-a[0], a[0]))
    #print(answer)
    return answer[0]

# print(solution([1, 2, 3, 4, 5], 7))
# print(solution([1, 1, 1, 2, 3, 4, 5], 5))
# print(solution([2, 2, 2, 2, 2], 6))


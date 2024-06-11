#주사위 굴리기
#A의 주사위를 굴린 결과만 시뮬레이션해 6**(n/2) 가지에 대해 주사위 눈의 합을 저장
#B에 대해서도 마찬가지
import itertools

class Solution:
    def __init__(self, dice):
        self.dice = dice
        self.n = len(dice)
        self.A_choice_indices = []
        self.B_choice_indices = []
        #A에 대한 모든 가능한 조합의 합(저장)
        self.A_sums = []
        #B에 대한 모든 가능한 조합의 합(저장)
        self.B_sums = []

    def maximumWinningProbability(self):
        indices = [i for i in range(self.n)]
        choice = [0, 0]
        max_winning_count = -1
        for A_choice_indices in itertools.combinations(indices, self.n//2):
            self.A_choice_indices = A_choice_indices
            self.B_choice_indices = tuple(set(range(self.n))-set(A_choice_indices))
            self.A_dices = [self.dice[i] for i in self.A_choice_indices] #A가 선택한 주사위들
            self.B_dices = [self.dice[i] for i in self.B_choice_indices] #B가 선택한 주사위들
            count = self.winning_count()
            if max_winning_count < count:
                max_winning_count = count
                choice = self.A_choice_indices
        return list([i+1 for i in choice])


    def winning_count(self):
        #여기서 누적합 사용하기
        self.mystack = []
        #6^(n/2) 가지에 대해 주사위 눈의 합을 저장    
        self.dfs(0)
        count = 0
        for A_sum in self.A_sums:
            count += len(list(filter(lambda a: A_sum > a, self.B_sums)))
        
        self.A_sums = []
        self.B_sums = []
        return count


    def dfs(self, depth):
        if (depth == self.n//2):
        #self.A_sums, self.B_sums 업데이트하기
            A_sum = 0
            B_sum = 0
            for i, (A_dice, B_dice) in enumerate(zip(self.A_dices, self.B_dices)):
                A_sum += A_dice[self.mystack[i]] #주사위 눈의 합을 저장
                B_sum += B_dice[self.mystack[i]] #주사위 눈의 합을 저장
            self.A_sums.append(A_sum)
            self.B_sums.append(B_sum)
 
        else:
            for i in range(6):
                self.mystack.append(i)
                self.dfs(depth+1)
                self.mystack.pop()


def solution(dice):
    instance = Solution(dice)
    answer = instance.maximumWinningProbability()
    return answer

# instance = Solution(dice)
# instance.maximumWinningProbability()


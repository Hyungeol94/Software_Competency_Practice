import itertools
import bisect

class Solution:
    def __init__(self, dice):
        self.dice = dice
        self.n = len(dice)
        self.A_choice_indices = []
        self.B_choice_indices = []
        self.A_sums = []
        self.B_sums = []

    def maximumWinningProbability(self):
        indices = list(range(self.n))
        choice = []
        max_winning_count = -1

        for A_choice_indices in itertools.combinations(indices, self.n // 2):
            self.A_choice_indices = A_choice_indices
            self.B_choice_indices = tuple(set(indices) - set(A_choice_indices))
            self.A_dices = [self.dice[i] for i in self.A_choice_indices]
            self.B_dices = [self.dice[i] for i in self.B_choice_indices]
            
            count = self.winning_count()
            if count > max_winning_count:
                max_winning_count = count
                choice = self.A_choice_indices

        return [i + 1 for i in choice]

    def winning_count(self):
        self.A_sums = []
        self.B_sums = []
        
        self.dfs()

        self.A_sums.sort()
        self.B_sums.sort()

        count = 0
        for A_sum in self.A_sums:
            B_index = bisect.bisect_left(self.B_sums, A_sum)
            count += B_index

        return count

    def dfs(self):
        for indices in itertools.product(range(6), repeat=self.n // 2):
            A_sum = sum(self.A_dices[i][index] for i, index in enumerate(indices))
            B_sum = sum(self.B_dices[i][index] for i, index in enumerate(indices))
            self.A_sums.append(A_sum)
            self.B_sums.append(B_sum)

def solution(dice):
    instance = Solution(dice)
    return instance.maximumWinningProbability()
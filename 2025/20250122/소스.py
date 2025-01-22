#https://academy.elice.io/courses/78960/lectures/639680/lecturepages/7122027
#수학 성적

from typing import List
from fractions import Fraction

class Solution:
    def getFraction(self, larger: List[int], smaller: List[int]) -> [int]:
        """
        Calculate the fractional boundary given two scores.
        """
        A = larger[0]
        B = larger[1]
        C = smaller[0]
        D = smaller[1]
        
        numerator = -B + D
        denominator = A - B - C + D
        if denominator == 0:
            return [0, 1]  # Indicates no valid boundary
        return [numerator, denominator]

    def getMinMaxOfPossibleWeight(self, n: int, scores: List[List[int]], ranks: List[int]) -> List[int]:
        """
        Determine the minimum and maximum possible weights based on scores and ranks.
        """
        # Map ranks to their corresponding scores
        rank_map = {rank - 1: i for i, rank in enumerate(ranks)}
        lower_bound = 0
        upper_bound = 1

        for i in range(n - 1):
            larger = scores[rank_map[i]]
            smaller = scores[rank_map[i + 1]]
            [numerator, denominator] = self.getFraction(larger, smaller)
            bound = Fraction(numerator, denominator)

            if denominator > 0:
                lower_bound = max(lower_bound, bound)
            else:
                if 0 < numerator:
                    return [-1]
                upper_bound = min(upper_bound, bound)

        lower_bound = Fraction(lower_bound)
        upper_bound = Fraction(upper_bound)

        if 0 <= lower_bound <= upper_bound <= 1:
            return [lower_bound.numerator, lower_bound.denominator, upper_bound.numerator, upper_bound.denominator]
        else:
            return [-1]


# Input and execution
n = int(input())
scores = [list(map(int, input().split())) for _ in range(n)]
ranks = list(map(int, input().split()))

# Compute
instance = Solution()
res = instance.getMinMaxOfPossibleWeight(n, scores, ranks)
print(" ".join(map(str, res)))
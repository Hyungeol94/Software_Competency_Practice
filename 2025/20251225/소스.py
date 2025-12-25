#https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2025-12-25
#3075. Maximize Happiness of Selected Children

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)
        sorted_happiness = sorted(happiness, key=lambda a: -a)

        i = 0
        offset = 0
        acc = 0
        while i < k:
            acc += (max(0, sorted_happiness[i]-offset))
            offset += 1
            i += 1

        return acc
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i, num in enumerate(arr):
            if num % 2 == 0:
                count = 0
                continue
            count += 1
            if count == 3:
                return True
        return False
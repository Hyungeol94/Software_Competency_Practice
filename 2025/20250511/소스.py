#https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2025-05-11
#1550. Three Consecutive Odds

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        count = sum([True if num % 2 == 1 else False for num in arr[:3]])
        if count == 3:
            return True
        j = 0
        i = 3
        n = len(arr)
        while i < n:
            if arr[j] % 2 == 1:
                count -= 1
            if arr[i] % 2 == 1:
                count += 1
            if count == 3:
                return True
            i += 1
            j += 1
        return False
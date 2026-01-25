#https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/?envType=daily-question&envId=2026-01-25
#1984. Minimum Difference Between Highest and Lowest of K Scores

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        
        if k == 1:
            return 0

        #sliding window로 풀이
        arr = sorted(nums)
        n = len(nums)
        left = 0
        right = k-1
        difference = float('inf')
        while right < n:
            difference = min(difference, arr[right]-arr[left])
            right += 1
            left += 1
        
        return difference
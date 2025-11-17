#https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/?envType=daily-question&envId=2025-11-17
#1437. Check If All 1's Are at Least Length K Places Away

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -float('inf')
        for i, num in enumerate(nums):
            if num == 1:
                if i-prev <= k:
                    return False
                prev = i
        return True
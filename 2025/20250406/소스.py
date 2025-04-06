#https://leetcode.com/problems/largest-divisible-subset/?envType=daily-question&envId=2025-04-06
#368. Largest Divisible Subset

class Solution:
    def is_divisible(self, curr, other):
        if not (curr % other == 0 or other % curr == 0):
            return False
        return True
    
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
       
        @cache
        def dp(prev, i, state):
            if i == n:
                return []

            if state == 0: #해당 인덱스를 포함하지 않음
                #다음 것도 포함하지 않음
                res1 = dp(prev, i+1, 0) 
                res2 = []
                
                #다음 것을 포함함
                if i < n-1 and (prev == -1 or 0 <= prev and self.is_divisible(nums[i+1], nums[prev])): 
                    res2 = dp(prev, i+1, 1)
                return res1 if len(res1) > len(res2) else res2
            
            else: #해당 인덱스를 포함함
                res1 = [nums[i]] + dp(i, i+1, 0) #다음 것을 포함하지 않음
                res2 = []
                if i < n-1 and self.is_divisible(nums[i], nums[i+1]): #다음 것을 포함함
                    res2 = [nums[i]] + dp(i, i+1, 1)
                return res1 if len(res1) > len(res2) else res2
            
                
        res1 = dp(-1, 0, 0)
        res2 = dp(-1, 0, 1)

        return res1 if len(res1) > len(res2) else res2

#https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/?envType=daily-question&envId=2024-07-03

class Solution:
    def getDifference(self, left, right, nums: List[int]) -> int:
        return nums[len(nums)-1-right]-nums[left]

    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        answer = float('inf')
        for left in range(4):
            right = 3-left
            answer = min(answer, self.getDifference(left, right, nums))
        
        return answer

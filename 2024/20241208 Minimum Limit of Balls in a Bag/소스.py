import math

class Solution:
    def is_possible(self, nums, size_goal, maxOperations) -> bool:
        operation_count = 0
        for num in nums:
            operation_count += math.ceil(num / size_goal) -1 
        if operation_count <= maxOperations:
            return True
        return False

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            middle = (left + right) // 2
            if self.is_possible(nums, middle, maxOperations): #가능하다면 maximum 사이즈를 줄여보자
                right = middle
            else:
                left = middle+1
                
                
        return left
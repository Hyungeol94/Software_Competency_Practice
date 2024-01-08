# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    import itertools

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers)-1
        while(True):
            if numbers[L]+numbers[R] == target:
                return [L+1, R+1]
            if numbers[L]+numbers[R] < target:
                if L < len(numbers)-1:
                    L += 1
                    continue        
            if numbers[L]+numbers[R] > target:
                if R > 0:
                    R -= 1
                    continue
                
                    

                
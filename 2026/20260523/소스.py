#https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/?envType=daily-question&envId=2026-05-23
#1752. Check if Array Is Sorted and Rotated

class Solution:
    def check(self, nums: List[int]) -> bool:
        base = nums[0]
        prev = None
        is_dropped = False

        for num in nums:
            if not prev:
                prev = num
                continue
            
            if prev and prev <= num:
                if is_dropped and num > base:
                    return False
                
                prev = num
                continue
            
            if prev and prev > num:
                if is_dropped:
                    return False
                
                if base < num:
                    return False
                
                is_dropped = True
                prev = num
                continue
        
        return True
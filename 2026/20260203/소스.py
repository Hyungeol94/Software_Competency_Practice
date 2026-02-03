#https://leetcode.com/problems/trionic-array-i/?envType=daily-question&envId=2026-02-03
#3637. Trionic Array I

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        phase = 0
        n = len(nums)
        prev = None
        p = 0
        q = 0

        for i, num in enumerate(nums):
            if prev == num:
                return False
                
            if phase == 0:
                if prev and prev < num:
                    prev = num
                    continue
                elif prev and prev > num:
                    p = i-1
                    phase += 1
                    prev = num
                    continue
                else:
                    prev = num
                    continue

            elif phase == 1:
                if prev and prev > num:
                    prev = num
                    continue
                elif prev and prev < num:
                    q = i-1
                    phase += 1
                    prev = num
                    continue
                else:
                    prev = num
                    continue
            
            else:
                if prev and prev < num:
                    prev = num
                    continue
                elif prev and prev > num:
                    return False
                else:
                    prev = num
                    continue
        
        if 0 < p < q < n-1:
            return True
        return False
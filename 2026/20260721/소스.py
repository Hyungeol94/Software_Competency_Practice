#https://leetcode.com/problems/maximize-active-section-with-trade-i/description/?envType=daily-question&envId=2026-07-21
#3499. Maximize Active Section with Trade I

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        indices = [0]
        is_one = True
        n = len(s)
       
        for i, c in enumerate(s):
            if int(c) == (1 if is_one else 0):
                continue
            indices.append(i)
            is_one = not is_one

        indices.append(n)
        max_val = s.count('1')
        acc = max_val
        prefix = 0
        suffix_val = []
        prefix_val = []
        for i in range(n):
            suffix_val.append(acc)
            if s[i] == '1':
                acc -= 1
        for i in range(n):
            if s[i] == '1':
                prefix += 1
            prefix_val.append(prefix)
        
    
        left = 0
        right = 4
        while right < len(indices):
            val = indices[right] - indices[left]
            if right+1 < len(indices):
                val += indices[right+1]-indices[right]
            if right+1 < len(indices) and indices[right+1] < n:
                val += suffix_val[indices[right+1]]
            if 0<= left-1:
                val += prefix_val[indices[left-1]]
            
            max_val = max(max_val, val)
            left += 2
            right += 2
        return max_val
        
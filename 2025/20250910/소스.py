#https://leetcode.com/problems/minimum-number-of-people-to-teach/?envType=daily-question&envId=2025-09-10
#1733. Minimum Number of People to Teach

from copy import deepcopy

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        language_masks = []
        for i, arr in enumerate(languages):
            mask = 0
            for num in arr:
                mask |= 1 << num-1
            language_masks.append(mask)

        minVal = float('inf')

        for i in range(n):
            new_language_mask = 1 << i
            num_teach = 0
            temp_masks = deepcopy(language_masks)
            for friendship in friendships:
                a, b = friendship
                a_mask = temp_masks[a-1]
                b_mask = temp_masks[b-1]
                if a_mask & b_mask:
                    continue
                if not new_language_mask & a_mask:
                    num_teach += 1
                    temp_masks[a-1] |= new_language_mask
                if not new_language_mask & b_mask:
                    num_teach += 1
                    temp_masks[b-1] |= new_language_mask
            minVal = min(minVal, num_teach)
        
        return minVal
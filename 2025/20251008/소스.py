#https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=daily-question&envId=2025-10-08
#2300. Successful Pairs of Spells and Potions

import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sorted_potions = sorted(potions)
        n = len(potions)
        arr = []
        for spell in spells:
            strength = int(math.ceil(success / spell))
            i = bisect.bisect_left(sorted_potions, strength)
            if i == n:
                arr.append(0)
            
            else:
                arr.append(n-i)
        
        return arr
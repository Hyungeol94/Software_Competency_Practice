#https://leetcode.com/problems/rabbits-in-forest/?envType=daily-question&envId=2025-04-20
#781. Rabbits in Forest

from collections import defaultdict

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq_dist = defaultdict(int)
        for answer in answers:
            freq_dist[answer] += 1

        count = 0
        for key, val in freq_dist.items(): 
            if val <= key+1:
                count += key+1
            else:
                count += (key+1) * math.ceil((val / (key+1)))
        
        return count
#https://leetcode.com/problems/alternating-groups-ii/?envType=daily-question&envId=2025-03-09
#3208. Alternating Groups II

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
    
        #불가능한 경우
        if n < k:
            return 0
        
        count = 2
        prev = colors[0]
        left = 0
        right = 1
        numGroups = 0
        while left < n and right < n*2:
            if colors[right % n] != prev:
                if count == k:
                    numGroups += 1
                    left += 1
                else:
                    count += 1

            else: 
                left = right
                count = 2
            
            prev = colors[right % n]
            right += 1
        return numGroups
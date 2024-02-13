class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        #Try all possible cuts for the array.
        n = len(jobDifficulty)
        cut = 0 #처음 시작 인덱스는 전체
        @cache
        def dp(cut, d):
            if n<d:
                return -1

            if d == 0:
                return 0
            
            if d == 1:
                return max(jobDifficulty[cut:])
            
            minDiff = float('inf')
            for i in range(cut+1, n-(d-1)+1): #d-1만큼은 남겨놓아야 함
                minDiff = min(minDiff, max(jobDifficulty[cut:i])+ dp(i, d-1))

            return minDiff if minDiff != float('inf') else -1
        
        return dp(0, d)
            
                

    
        
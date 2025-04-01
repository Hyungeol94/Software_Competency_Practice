#https://leetcode.com/problems/solving-questions-with-brainpower/submissions/1592883079/?envType=daily-question&envId=2025-04-01
#2140. Solving Questions With Brainpower

from functools import cache

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        @cache
        def dp(i):
            if n <= i:
                return 0

            curr_point, curr_brainpower = questions[i]

            if i == n-1:
                return curr_point

            maxVal = curr_point + dp(i+curr_brainpower+1)
            for j in range(i+1, n):
                curr_point, curr_brainpower = questions[j]
                maxVal = max(maxVal, curr_point + dp(j+curr_brainpower+1))
            
            return maxVal
        
        return dp(0)
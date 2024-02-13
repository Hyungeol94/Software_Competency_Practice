class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        #dp(i, left) return the maximum possible score if we have already done i total operations and used left numbers from the left side.
        #To answer the original problem, we should return dp(0, 0)
        #이미 i까지의 연산을 끝냈고, 현재 left의 위치의 인덱스가 주어져 있을 때, 남은 숫자 리스트와 연산자들을 가지고 도출할 수 있는 최적의 해를 찾을 수 있어야 함
        @cache
        def dp(i, left):
            if i == m:
                return 0  
            right = n-1-(i-left)
            mult = multipliers[i]
            return max(dp(i+1, left+1)+nums[left]*mult, dp(i+1, left)+nums[right]*mult)

        n, m = len(nums), len(multipliers)
        return dp(0, 0)


        

    

    
    
   

       
        
        
            
        
#https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #state: 이전에 선택된 숫자, index 두 가지 있어야 함
        n = len(nums)
        @lru_cache(50000)
        def dp(limit, i):
            if i == n-1:
                answer = 1 if limit < nums[i] else 0
                return answer
            
            if limit < nums[i]: #i번째 수가 선택 가능한 상황이라면
                return max(1+dp(nums[i], i+1), dp(limit, i+1))
            else:
                return dp(limit, i+1)
       
        return dp(-float('inf'), 0)
        


        
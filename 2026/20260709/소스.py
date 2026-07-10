#https://leetcode.com/problems/path-existence-queries-in-a-graph-i/?envType=daily-question&envId=2026-07-09
#Path Existence Queries in a Graph I

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        next = [-1]*n
        left = 0
        right = 0
        while left < n:
            while right < n and nums[right]-nums[left] <= maxDiff:
                right += 1
            next[left] = right-1
            left += 1

        @cache
        def dp(k): #max reach를 반환
            if next[k] == k:
                return k
                
            return dp(next[k])

        ans = []
        for k, v in queries:
            if k > v:
                k, v = v, k
            ans.append(True if dp(k) >= v else False)
        return ans 

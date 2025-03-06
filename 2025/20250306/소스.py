#https://leetcode.com/problems/find-missing-and-repeated-values/
#2965. Find Missing and Repeated Values

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        composite = set([i for i in range(1, n ** 2+1)])
        seen = set()
        ans = []
        for row in grid:
            for item in row:
                if item in seen:
                    ans.append(item)
                seen.add(item)
        
        ans += list(composite - seen)
        return ans
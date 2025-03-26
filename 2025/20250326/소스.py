#https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/?envType=daily-question&envId=2025-03-26
#2033. Minimum Operations to Make a Uni-Value Grid

import bisect

class Solution:
    def get_count(self, base, items, x):
        count = 0
        for item in items:
            count += abs(base-item) // x
        return count

    def minOperations(self, grid: List[List[int]], x: int) -> int:
        #2 4 6 8에서 골라야 함 -> 4 혹은 6임
        acc = 0
        n = len(grid)
        m = len(grid[0])
        if n == 1 and m == 1:
            return 0

        remainder = grid[0][0] % x
        items = []
        for row in grid:
            items += row
            for item in row:
                acc += item
                #나머지가 모두 같은 경우만 취급
                if item % x != remainder:
                    return -1

        items.sort()
        minVal, maxVal = items[0], items[-1]
        avg, remainder = divmod(acc, m*n)
        candidates = range(minVal, maxVal+1, x)
        idx = bisect.bisect_left(candidates, avg)
        
        #꺾이는 지점까지 greedy하게 찾아가기
        offset = 1
        if idx != len(candidates)-1:
            if self.get_count(candidates[idx], items, x) < self.get_count(candidates[idx+offset], items, x):
                offset = -1
        else:
            offset = -1

        minVal = self.get_count(candidates[idx], items, x)

        while True:
            idx = idx+offset
            if not 0 <= idx < len(candidates):
                break
            curr = self.get_count(candidates[idx], items, x)
            if curr < minVal:
                minVal = curr
            else:
                break
        
        return minVal
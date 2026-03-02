#https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/?envType=daily-question&envId=2026-03-02
#1536. Minimum Swaps to Arrange a Binary Grid

from functools import reduce

class Solution:
    def mostRightIndex(self, row) -> int:
        def f(acc, b):
            if b[1]:
                return b[0]
            return acc

        return reduce(f, enumerate(row), 0)
        

    def minSwaps(self, grid: List[List[int]]) -> int:
        mostRight = list(map(lambda row: self.mostRightIndex(row), grid))
        if not all([index <= i for i, index in enumerate(sorted(mostRight))]):
            return -1

        n = len(grid)

        countSwap = 0
        for i in range(n):
            if mostRight[i] <= i:
                continue
            
            index = 0
            for j in range(i+1, n):
                if mostRight[j] <= i:
                    index = j
                    break

            countSwap += index-i

            while index > i:
                mostRight[index], mostRight[index-1] = mostRight[index-1], mostRight[index]
                index -= 1
        
        return countSwap
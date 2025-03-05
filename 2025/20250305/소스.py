class Solution:
    def coloredCells(self, n: int) -> int:
        i = 0
        val = 1
        while i <= n-1:
            val += i*4
            i += 1
        return val
    
    def coloredCells2(self, n: int) -> int:
        return int(4 * n * (n-1)/2) + 1
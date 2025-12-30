#https://leetcode.com/problems/magic-squares-in-grid/?envType=daily-question&envId=2025-12-30
#840. Magic Squares In Grid

class Solution:
    def isMagicSquare(self, grid, i, j):
        seen = set()

        for p in range(i, i+3):
            for q in range(j, j+3):
                if (grid[p][q]) in seen:
                    return False
                if not 1 <= grid[p][q] <= 9:
                    return False
                seen.add(grid[p][q])
        
        magic_num = sum([item for item in grid[i][j:j+3]])
        
        #row check
        for row in grid[i:i+3]:
            if sum([item for item in grid[i][j:j+3]]) != magic_num: 
                return False
        
        #col check
        for q in range(j, j+3):
            acc = 0
            for p in range(i, i+3):
                acc += grid[p][q]
            if acc != magic_num:
                return False
        
        #diagonal check 
        acc = 0
        index = j
        for row in grid[i:i+3]:
            acc += row[index]
            index += 1
        if acc != magic_num:
            return False
        
        acc = 0
        index = j+2
        for row in grid[i:i+3]:
            acc += row[index]
            index -= 1
        if acc != magic_num:
            return False

        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if n < 3 or m < 3:
            return 0
        
        count = sum([sum([self.isMagicSquare(grid, i, j) for j in range(m-2)]) for i in range(n-2)])
        return count


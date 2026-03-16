#https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/?envType=daily-question&envId=2026-03-16
#1878. Get Biggest Three Rhombus Sums in a Grid

class Solution:
    def computeRombusSum(self, grid, rombus_diagonal_blocks, sums):
        m, n = len(grid), len(grid[0])
        #edge case
        if rombus_diagonal_blocks == 1:
            for i in range(m):
                for j in range(n):
                    sums.add(grid[i][j])
            return

        #grid[i][j]가 center
        dr_offsets = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
        center_offset = (rombus_diagonal_blocks // 2)

        for i in range(m):
            if i - center_offset < 0 :
                continue
            if i + center_offset >= m:
                break
            for j in range(n):
                if j - center_offset < 0:
                    continue
                if j + center_offset >= n:
                    break
                #시작 위치
                p, q = i, j - center_offset
                dr_index = 0
                acc = 0
                while dr_index < len(dr_offsets):
                    count = 0
                    while count < center_offset :
                        p += dr_offsets[dr_index][0]
                        q += dr_offsets[dr_index][1]
                        acc += grid[p][q]
                        count += 1
                    dr_index += 1
                sums.add(acc)

        return
           
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        rombus_diagonal_blocks = 1
        sums = set()
        while rombus_diagonal_blocks <= min(m, n): 
            #brute-force 탐색
            self.computeRombusSum(grid, rombus_diagonal_blocks, sums)
            rombus_diagonal_blocks += 2
        
        return sorted(list(sums), reverse = True)[:3]
//https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/?envType=daily-question&envId=2026-04-28
//2033. Minimum Operations to Make a Uni-Value Grid

/**
 * @param {number[][]} grid
 * @param {number} x
 * @return {number}
 */
var minOperations = function(grid, x) {
    const n = grid.length
    const m = grid[0].length
    
    const arr = []
    const offset = grid[0][0] % x
    for (let i = 0; i < n; i++) { 
        for (let j = 0; j < m; j++) { 
            const num = grid[i][j]
            if ((num % x) != offset) { 
                return -1
            }
            arr.push(grid[i][j] - offset)
        }
    }
    arr.sort((a, b) => a - b)
    const num = arr[Math.floor(arr.length / 2)]
    
    let ans = 0
    for (let i = 0; i < n; i++) { 
        for (let j = 0; j < m; j++) { 
            ans += Math.abs(grid[i][j] - offset - num) / x
        }
    }

    return ans
};